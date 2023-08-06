const _ = require('lodash');

const Constants = require('../utils/constants');
const { ReportType } = require('../reports/report');
const { SecurityActivity } = require('../reports/security_activity');
const { Event } = require('../reports/event');
const HeartbeatCache = require('../reports/heartbeat_cache');
const Logger = require('../utils/logger');

function createSecurityActivity(data) {
  let sessionId = null;
  try {
    if (_.isArray(data.data) && data.data[0] && data.data[0].poSessionId) {

      return mapEventsAndGetAction(data.data, data.data[0].poSessionId);
    }
  } catch (error) {
    Logger.write(
      Logger.ERROR && `Error occurred while storing stackTace : ${error}`
    );
  }
  return {
    action: ReportType.REPORT_TYPE_NONE,
    sessionId
  };
}

function storeStackTrace(data) {
  let sessionId = null;
  try {
    if (_.isArray(data.data) && data.data[0] && data.data[0].poSessionId) {
      sessionId = data.data[0].poSessionId;
      return mapEventsAndGetAction(data.data, sessionId);
    }
  } catch (error) {
    Logger.write(
      Logger.ERROR && `Error occurred while storing stackTace : ${error}`
    );
  }
  return {
    action: ReportType.REPORT_TYPE_NONE,
    sessionId
  };
}

function mapEvents(eventsToMap) {
  try {
    let blocked = false;
    const mappedEvents = eventsToMap.reduce((acc, event) => {
      if (
        _.isString(event.eventType) &&
        event.reportType &&
        event.poSessionId &&
        event.resultName
      ) {
        blocked = blocked || event.reportType === ReportType.REPORT_TYPE_BLOCK;

        acc.push(
          new Event(
            event.eventType,
            event.poSessionId,
            event.reportType === ReportType.REPORT_TYPE_BLOCK,
            event.resultConfidence,
            new Date(),
            new Date(),
            event.resultName,
            '',
            event.resultMessage,
            500,
            event.stackTrace
          )
        );
      }
      return acc;
    }, []);
    const action = blocked ?
      (mappedEvents.every((event) => event.category === Constants.WAF_EVENT_TYPE) ?
        ReportType.REPORT_TYPE_ABORT :
        ReportType.REPORT_TYPE_BLOCK) :
      ReportType.REPORT_TYPE_NONE;
    return {
      mappedEvents,
      action
    };
  } catch (e) {
    Logger.write(Logger.DEBUG && `Failed to mapEvents with error: ${e}`);
    return {};
  }
}

function generateWafEvents(data) {
  let sessionId = null;
  try {
    const findings = data.data.findings;
    if (!_.isArray(findings)) {
      return {
        events: [],
        shouldCollectStacktrace: false
      };
    }
    sessionId = data.data.poSessionId;
    let events = [];
    for (let finding of findings) {
      events.push({
        eventType: Constants.WAF_EVENT_TYPE,
        poSessionId: sessionId,
        reportType: finding.action,
        resultName: finding.flowName
      });
    }

    return mapEventsAndGetAction(events, sessionId);
  } catch (e) {
    Logger.write(Logger.ERROR && `Failed to generateWafEvents with error: ${e}`);
  }
  return {
    action: ReportType.REPORT_TYPE_NONE,
    sessionId
  };
}

function mapEventsAndGetAction(events, sessionId) {
  try {
    const { mappedEvents, action } = mapEvents(
      events
    );
    if (_.isArray(mappedEvents) && _.isString(action)) {
      const securityActivity = new SecurityActivity(sessionId);
      securityActivity.events.push(...mappedEvents);

      HeartbeatCache.cacheReportEvents(securityActivity);
      return {
        action,
        sessionId
      };
    }
  } catch (error) {
    Logger.write(Logger.ERROR && `Failed to mapEventsAndGetAction with error: ${e}`);
  }
  return {
    action,
    sessionId
  };
}

module.exports = {
  createSecurityActivity,
  generateWafEvents,
  storeStackTrace
};
