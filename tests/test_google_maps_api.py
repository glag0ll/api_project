from utils.api import GoogleMapsApi
from requests import Response

class TestCreatePlace():

    def test_create_new_place(self):

        google_maps_api = GoogleMapsApi()

        print('\nМетод POST')
        result_post: Response = google_maps_api.create_new_place()