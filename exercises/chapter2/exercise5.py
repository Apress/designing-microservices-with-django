import time


class RateLimitMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limiter_cache = {}

    def _get_client_ip(self, request):
        client_ip = request.META.get('REMOTE_ADDR')
        forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
        if forwarded:
            client_ip = forwarded.split(',')[0]
        return client_ip

    def __call__(self, request):
        client_ip = self._get_client_ip(request)
        call_timestamp = time.time()
        client_call_timestamps = self.rate_limiter_cache.get(client_ip, [])
        
        relevant_calls = [
            timestamp for timestamp in client_call_timestamps 
            if timestamp > round(call_timestamp) - 3600
        ]
        if len(relevant_calls) > 100:
            raise Exception("rate limit reached")

        response = self.get_response(request)

        relevant_calls.append(call_timestamp)
        self.rate_limiter_cache[client_ip] = relevant_calls

        return response
