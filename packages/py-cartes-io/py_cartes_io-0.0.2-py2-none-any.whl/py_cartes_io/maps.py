import requests


class Maps():

    API_URL = 'https://cartes.io/api/'
    API_KEY = None

    def __init__(self, map_uuid=None, api_key=None):

        self.map_uuid = map_uuid

        if api_key is not None:
            self.api_key = api_key
        else:
            self.api_key = self.API_KEY

        self.request = None

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

        response = requests.get(self.request)

        if response.status_code == 200:
            return response.json()
        else:
            print('Error: {}'.format(response.status_code))
            return None

    def create(self, data):
        if (not self.request):
            self.request = 'https://cartes.io/api/maps'.format(
                self.map_uuid)

        headers = {'Content-type': 'application/json',
                   'Accept': 'application/json'}
        try:
            response = requests.post(
                self.request, json=data, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                print('Error: {}'.format(response.status_code))
                # print message
                print(response.json())
        except Exception as e:
            print(e)
