from rest_framework.throttling import UserRateThrottle

class NEW_USER_RateThrottle(UserRateThrottle):
    scope = 'new_user'


