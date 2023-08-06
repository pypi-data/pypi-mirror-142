class CHClientException(BaseException): pass

class ImproperlyConfigured(CHClientException): pass

class UserNotConsented(CHClientException): pass

class DelegateStateError(CHClientException): pass

class HTTPError(CHClientException):

    def __init__(self, status_code):
        self.status_code = status_code
