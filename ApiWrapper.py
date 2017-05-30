import requests
import ast


class Request:

    def __init__(self, method_name, token=''):
        self.raw = 'https://api.vk.com/method/{0}?v=5.52&'.format(method_name)
        self.token = token

    def add_parameter(self, name, value):
        self.raw += '{0}={1}&'.format(name, value)

    def get_raw(self):
        if self.token != '':
            return '{0}access_token={1}'.format(self.raw, self.token)
        return self.raw[0: -1]
