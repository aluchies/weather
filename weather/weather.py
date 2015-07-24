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
        var = read_settings(api_key='None', zip_code='None')
        return var


    def get_api_key(self):
        var = self.get_config_vars()
        if var['api_key'] =='None':
            self.api_key = input_api_key()
            write_settings(api_key=self.api_key)
        else:
            self.api_key = var['api_key']





    def get_zip_code(self):
        var = self.get_config_vars()
        if var['zip_code']  == 'None':
            self.zip_code = input_zip_code()
            write_settings(zip_code=self.zip_code)
        else:
            self.zip_code = var['zip_code']



    def set_request_link(self):
        if self.api_key == None:
            self.get_api_key()

        if self.zip_code == None:
            self.get_zip_code()

        self.api_link = 'https://api.wunderground.com/api/' + \
                        str(self.api_key) + '/forecast/q/' + \
                        str(self.zip_code) + '.json'


    def get_forecast(self):
        if self.api_link == None:
            self.set_request_link()


        self.json = requests.get(self.api_link).json()
        self.response = self.json['response']
        if 'error' in self.response.keys():
            raise ValueError('api_key or zip_code are incorrect')
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







def write_settings(api_key='None', zip_code='None'):
    settings = read_settings(api_key=api_key, zip_code=zip_code)

    cfile = os.path.join(os.getenv("HOME"), '.weather', 'config.txt')

    if not os.path.isdir(os.path.join(os.getenv("HOME"), '.weather')):
        os.mkdir(os.path.join(os.getenv("HOME"), '.weather'))

    if not os.path.isfile(cfile):
        with open(cfile, 'w') as f:
            f.write('')

    with open(cfile, 'w') as f:
        for item in settings.keys():
            f.write(item + '=' + str(settings[item]) + '\n')




def read_settings(api_key='None', zip_code='None'):

    settings = {'api_key' : api_key, 'zip_code' : zip_code}

    cfile = os.path.join(os.getenv("HOME"), '.weather', 'config.txt')

    if os.path.isfile(cfile):
        with open(cfile, 'r') as f:
            readlines = f.readlines()

        for line in readlines:
            items = line.strip('\n').split('=')

            if items[0] in settings.keys():
                settings.update({items[0]: items[1]})

    if api_key != 'None':
        settings['api_key'] = api_key
    if zip_code != 'None':
        settings['zip_code'] = zip_code

    return settings



def input_api_key():
    api_key = raw_input("Please enter your wunderground.com api key: ")
    return api_key

def input_zip_code():
    zip_code = raw_input("Please enter your zip code: ")
    return zip_code





def main():
    f = Forecast()

    print f.get_period_high(0)

if __name__ == '__main__':
    main()