const RuleSet = require('./ruleset');
const Metrics = require('./metrics');
const DataFrame = require('./dataFrame');
const WAFallowList = require('./allowList/allowlist_manager');
require('../../utils/common_utils');
const _ = require('lodash');
const qs = require('qs');
const Logger = require('../../utils/logger');
const { ReportType } = require('../../reports/report');

class WAF {
    constructor(ruleSetDef, context) {
        this.context = context || {};
        this.metrics = this.context.metrics =
            this.context.metrics || new Metrics();
        this.updateRuleset(ruleSetDef);
    }

    updateRuleset(newRulesetDef) {
        this.AllowListManager = new WAFallowList(newRulesetDef);
        this.ruleset = new RuleSet(newRulesetDef, this.context);
    }

    createDataFrame() {
        return new DataFrame(this.ruleset);
    }

    scanRequestParams(requestData) {
        let result = {
            action: ReportType.REPORT_TYPE_NONE
        };
        try {
            const request = this.context.poContext.get(
                requestData.data.poSessionId
            );
            if (
                !_.isObject(request.pathParams) &&
                !_.isObject(request.queryParams)
            ) {
                return result;
            }
            Logger.write(
                Logger.DEBUG &&
                `waf: Scanning http headers: ${requestData.data.poSessionId}, request: ${request}`
            );
            const findings = this.checkHTTPRequest({
                pathParams: request.pathParams,
                queryParams: request.queryParams
            });
            return {
                findings: findings,
                poSessionId: requestData.data.poSessionId
            };
        } catch (e) {
            Logger.write(
                Logger.DEBUG && `waf: Failed to scan http data data: ${e}`
            );
        }
        return result;
    }

    scanHttpHeaders(requestData) {
        let result = {
            action: ReportType.REPORT_TYPE_NONE
        };
        try {
            const request = this.context.poContext.get(
                requestData.data.poSessionId
            );
            if (!_.isObject(request.requestHeaders)) {
                return result;
            }
            Logger.write(
                Logger.DEBUG &&
                `waf: Scanning http headers: ${requestData.data.poSessionId}, request: ${request}`
            );
            const findings = this.checkHTTPRequest({
                requestHeaders: request.requestHeaders
            });
            return {
                findings: findings,
                poSessionId: requestData.data.poSessionId
            };
        } catch (e) {
            Logger.write(
                Logger.DEBUG && `waf: Failed to scan http data data: ${e}`
            );
        }
        return result;
    }

    scanHttpBody(requestData) {
        let result = {
            action: ReportType.REPORT_TYPE_NONE
        };
        try {
            if (
                !requestData.data.requestBody ||
                !_.isBuffer(requestData.data.requestBody)
            ) {
                return result;
            }

            const request = this.context.poContext.get(
                requestData.data.poSessionId
            );
            let requestToCheck = {
                body: {}
            };
            const contentTypeHeader = request.requestHeaders && request.requestHeaders['content-type'];
            if (_.isValidJsonRequest(contentTypeHeader)) {
                requestToCheck.body.raw = requestData.data.requestBody.toString();
            }
            if (_.isValidEncodedFormDataRequest(contentTypeHeader)) {
                requestToCheck.body.raw = JSON.stringify(qs.parse(inputData.requestBody.toString()));
            }
            if (_.isValidMultipartFormDataRequest(contentTypeHeader)) {
                if (requestData.data.formData && _.isArray(requestData.data.formData.filenames) && requestData.data.formData.filenames.length) {
                    requestToCheck.body.filenames = requestData.data.formData.filenames;
                    requestToCheck.body.files_field_names = requestData.data.formData.filesFieldNames;
                    requestToCheck.body.combined_file_size = requestData.data.formData.combinedFileSize.toString();
                }
                if (_.isObject(requestData.data.formData.fields)) {
                    requestToCheck.body.raw = JSON.stringify(requestData.data.formData.fields);
                }
            }

            Logger.write(
                Logger.DEBUG &&
                `waf: Scanning http body: ${requestData.data.poSessionId}, request: ${requestToCheck.body}`
            );
            const findings = this.checkHTTPRequest(requestToCheck);
            return {
                findings: findings,
                poSessionId: requestData.data.poSessionId
            };
        } catch (e) {
            Logger.write(
                Logger.DEBUG && `httpServer: Failed to store session data ${e}`
            );
        }

        return result;
    }

    checkHTTPRequest(request, dataFrame /*optional*/) {
        if (this.AllowListManager.shouldBypassRequest(request)) {
            return Promise.resolve([]);
        }
        if (request.queryParams) {
            request.queryParams =
                this.AllowListManager.filterParameters(request);
        }
        dataFrame = dataFrame || this.createDataFrame();

        let findings = [];
        this.ruleset.mapData(
            'http.request',
            request,
            (targetName, valueList) => {
                dataFrame.addAndCheckCB(
                    targetName,
                    (finding) => {
                        findings.push(finding);
                    },
                    () => {
                        /* this target done */
                    },
                    ...valueList
                );
            },
            () => {
                /* all fields done */
                // Do nothing
            }
        );
        return findings;
    }
}

WAF.DataFrame = DataFrame;

module.exports = WAF;
