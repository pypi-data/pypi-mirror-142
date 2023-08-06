class Event {
  constructor(
    category,
    request_id,
    blocked,
    confidence_level,
    date,
    date_started,
    type,
    duration,
    security_response,
    status,
    stackTrace
  ) {
    (this.category = category),
      (this.request_id = request_id),
      (this.blocked = blocked),
      (this.confidence_level = confidence_level),
      (this.date = date || new Date()),
      (this.date_started = date_started || new Date()),
      (this.type = type),
      (this.duration = duration),
      (this.security_response = security_response),
      (this.status = status);
      (this.stackTrace = stackTrace);
  }
}

class WAFEvent extends Event {
  constructor(request_id, blocked, type, stackTrace) {
    super('waf', request_id, blocked, 50, new Date(), new Date(), type, 0, 'response', 'status', stackTrace);
  }
}

module.exports = {
  Event,
  WAFEvent
};
