import json


class B2BAPIException(Exception):

    def __init__(self, response, status_code, text):
        self.code = 0
        try:
            json_res = json.loads(text)
        except ValueError:
            self.message = 'Invalid JSON error message from B2BinPay: {}'.format(response.text)
        else:
            self.code = json_res['errors'][0]['code']
            self.message = json_res['errors']
        self.status_code = status_code
        self.response = response
        self.request = getattr(response, 'request', None)

    def __str__(self):
        return 'APIError(code=%s): %s' % (self.code, self.message)


class B2BRequestException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'B2BRequestException: %s' % self.message
