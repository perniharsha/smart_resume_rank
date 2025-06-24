from prometheus_client import Summary, Counter

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
MATCH_COUNT = Counter('match_requests_total', 'Total scoring requests')
