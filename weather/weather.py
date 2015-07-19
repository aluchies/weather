import requests
import os

class Forecast(object):
    """

    """

    def __init__(self):
        self.zip_code = None
        self.api_key = None
        self.api_link = None
        self.json = None
        self.forecast = None

    def get_config_vars(self):
        config = open(os.path.join('config.txt'), 'r')
        lines = config.read().split('\n')
        var = {}
        for line in lines:
            entry = []
            for items in line.split('='):
                entry.append(items.strip())
            var.update(dict([entry]))

        return var


    def get_api_key(self):
        var = self.get_config_vars()
        if 'api_key' in var:
            self.api_key = var['api_key']


    def get_zip_code(self):
        var = self.get_config_vars()
        if 'zip_code' in var:
            self.zip_code = var['zip_code']


    def set_request_link(self):
        if self.api_key == None:
            self.get_api_key()

        if self.zip_code == None:
            self.get_zip_code()

        self.api_link = 'https://api.wunderground.com/api/' + \
                        self.api_key + '/forecast/q/' + self.zip_code + '.json'

    def get_forecast(self):
        if self.api_link == None:
            self.set_request_link()


        self.json = requests.get(self.api_link).json()
        self.response = self.json['response']
        if 'forecast' in self.json.keys():
            self.forecast = self.json['response']
        else:
            self.forecast = None

    def get_period_forecast(self, period):
        if self.forecast == None:
            self.get_forecast()
        return self.json['forecast']['simpleforecast']['forecastday'][period]

    def get_period_high(self, period):
        period_data = self.get_period_forecast(period)
        high = period_data['high']['fahrenheit']
        return 'High: ' + str(high) + 'F'

def main():
    f = Forecast()

    print f.get_period_high(0)

if __name__ == '__main__':
    main()