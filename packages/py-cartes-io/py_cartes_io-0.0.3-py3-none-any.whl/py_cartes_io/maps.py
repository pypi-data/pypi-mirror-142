import time
import requests

# seconds (multiplies by 3 for create map endpoint)
MIN_TIME_BETWEEN_REQUESTS = 2


class Maps():

    API_URL = 'https://cartes.io/api/'
    API_KEY = None
    LAST_REQUEST_TIME = 0

    def __init__(self, map_uuid=None, api_key=None):

        self.map_uuid = map_uuid

        if api_key is not None:
            self.api_key = api_key
        else:
            self.api_key = self.API_KEY

        self.request = None

        self.headers = {'Content-type': 'application/json',
                        'Accept': 'application/json'}

    def markers(self):
        # Get the markers
        self.request = 'https://cartes.io/api/maps/{}/markers'.format(
            self.map_uuid)
        return self

    def get(self):

        # Get the map
        if (not self.request):
            self.request = 'https://cartes.io/api/maps'
            if self.map_uuid is not None:
                self.request += '/{}'.format(self.map_uuid)

        # If not enough time has passed since the last request, wait
        if (time.time() - self.LAST_REQUEST_TIME) < MIN_TIME_BETWEEN_REQUESTS:
            time.sleep(MIN_TIME_BETWEEN_REQUESTS)

        response = requests.get(self.request)

        self.LAST_REQUEST_TIME = time.time()

        if response.status_code == 200:
            return response.json()
        else:
            print('Error: {}'.format(response.status_code))
            return None

    def create(self, data):
        if (not self.request):
            self.request = 'https://cartes.io/api/maps'.format(
                self.map_uuid)
        try:
            # If not enough time has passed since the last request, wait
            if (time.time() - self.LAST_REQUEST_TIME) < MIN_TIME_BETWEEN_REQUESTS * 3:
                time.sleep(MIN_TIME_BETWEEN_REQUESTS * 3)

            response = requests.post(
                self.request, json=data, headers=self.headers)

            self.LAST_REQUEST_TIME = time.time()

            if response.status_code == 200:
                return response.json()
            else:
                print('Error: {}'.format(response.status_code))
                # print message
                print(response.json())
        except Exception as e:
            print(e)
