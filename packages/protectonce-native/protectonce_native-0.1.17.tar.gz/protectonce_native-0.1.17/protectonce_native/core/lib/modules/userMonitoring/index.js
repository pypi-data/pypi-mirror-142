const { SecurityActivity } = require('../../reports/security_activity');
const { Event } = require('../../reports/event');
const HeartbeatCache = require('../../reports/heartbeat_cache');
const Logger = require('../../utils/logger');
const userManager = require('./user_manager');
const ProtectOnceContext = require('../context');
const { ReportType } = require('../../reports/report');

/* This method creates securityActivity object for signUp data of user
* It adds signup event in Event object inside SecurityActivity object 
* It also returns action object with values (allow and block) based 
  on userName passed is in blocked user list
* @param  {Object} signUpData - signUp data received as input
*          @param {Object} data This holds actual signup data
*              @param {String} poSessionId
*              @param {String} userName
*/
function storeSignUpData(signUpData) {
    try {
        const poSessionId = signUpData.data.poSessionId;
        const userName = signUpData.data.userName;
        const userData = { "poSessionId": poSessionId, "userName": userName, "status": "success" };
        const event = getEvent(userData, "signup");
        Logger.write(Logger.DEBUG && `calling storeSignUpData with userName : ${userName}`);
        createSecurityActivity(poSessionId, createUser(userName), event);
        return { "result": { "action": getAction(userName) } };
    } catch (e) {
        Logger.write(Logger.DEBUG && `Failed calling storeSignUpData with error : ${e}`);
        return { "result": { "action": ReportType.REPORT_TYPE_NONE } };
    }
}

function createUser(userName) {
    return {
        "identifier": userName
    }
}

/* This method creates securityActivity object for login data of user
* It adds login event in Event object inside SecurityActivity object 
* It also returns action object with values (allow and block) based 
  on userName passed is in blocked user list
* @param  {Object} loginData - loginData received as input
*          @param {Object} data This holds actual login data
*              @param {String} poSessionId
*              @param {String} success
*              @param {String} userName
*/
function storeLoginData(loginData) {
    try {
        const poSessionId = loginData.data.poSessionId;
        const success = loginData.data.success;
        const userName = loginData.data.userName;
        const userData = { "poSessionId": poSessionId, "userName": userName, "status": success ? "success" : "failure" };
        const event = getEvent(userData, "login");
        Logger.write(Logger.DEBUG && `calling storeLoginData with status : ${success} ` && `userName : ${userName}`);
        createSecurityActivity(poSessionId, createUser(userName), event);
        return { "result": { "action": getAction(userName) } };
    } catch (e) {
        Logger.write(Logger.DEBUG && `Failed calling storeLoginData with error : ${e}`);
        return { "result": { "action": ReportType.REPORT_TYPE_NONE } };
    }
}


function getEvent(userData, eventType) {

    const isBlockedUser = userManager.isUserInBlockedList(userData.userName);
    const status = isBlockedUser ? 'failure' : userData.status;

    const event = new Event("", userData.poSessionId, false, "", new Date(),
        new Date(), eventType, "", "", status);
    return event;
}

function getAction(userName) {
    return userManager.isUserInBlockedList(userName) ? ReportType.REPORT_TYPE_BLOCK : ReportType.REPORT_TYPE_NONE;
}


function createSecurityActivity(poSessionId, user, event) {
    const context = ProtectOnceContext.get(poSessionId);
    const securityActivity = new SecurityActivity(poSessionId, "status", context.sourceIP, "200", context.method, context.path, user);
    if (event) {
        securityActivity.addEvent(event);
    }
    HeartbeatCache.cacheReport(securityActivity);
}

/*This method creates securityActivity object for user details 
* It adds user object inside securityActivity object with identifier as key and 
* userName as value
* It also returns action object with values (allow and block) based 
  on userName passed is in blocked user list
* @param  {Object} identifyData - identifyData received as input
*          @param {Object} data This holds actual user data
*              @param {String} poSessionId
*              @param {String} userName
*/
function identify(identifyData) {
    try {
        const poSessionId = identifyData.data.poSessionId;
        const userName = identifyData.data.userName;
        const isBlockedUser = userManager.isUserInBlockedList(userName);
        let action = "success";
        if (isBlockedUser) {
            action = "block";
        }
        createSecurityActivity(poSessionId, createUser(userName));
        return { "result": { "action": getAction(userName) } };
    } catch (e) {
        Logger.write(Logger.DEBUG && `Failed calling identify with error : ${e}`);
        return { "result": { "action": ReportType.REPORT_TYPE_NONE } };
    }
}

module.exports = {
    storeSignUpData: storeSignUpData,
    storeLoginData: storeLoginData,
    identify: identify
}

