import json

from utils.api import GoogleMapsApi
from requests import Response

class TestCreatePlace():

    def test_create_new_place(self):

        google_maps_api = GoogleMapsApi()

        print('\nметод POST')
        result_post = google_maps_api.create_new_place()

        check_post = result_post.json()
        place_id = check_post.get('place_id')

        print('\nметод GET')
        result_get = google_maps_api.get_new_place(place_id)