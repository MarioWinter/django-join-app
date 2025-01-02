from rest_framework.throttling import UserRateThrottle

class ContactThrottle(UserRateThrottle):
    scope = 'contact'
    #rate = '5/day'
    def allow_request(self, request, view):
        if request.method == 'GET':
            return True
        
        new_scope = 'contact-' + request.method.lower()
        if new_scope in self.THROTTLE_RATES:
            self.scope = new_scope
            self.rate = self.get_rate()
            self.num_requests, self.duration = self.parse_rate(self.rate)
        return super().allow_request(request, view)
    

