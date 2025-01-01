from rest_framework.throttling import UserRateThrottle

class ContactThrottle(UserRateThrottle):
    scope = 'contact'
    #rate = '5/day'
    def allow_request(self, request, view):
        if request.method == 'GET':
            return True
            #self.rate = '100/day'
        return super().allow_request(request, view)