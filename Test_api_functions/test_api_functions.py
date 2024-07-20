import pytest
import requests
from api_functions.API_functions import APIfuntions
from api_functions.mockData import TestData

class Test_API_Functions:

       @pytest.fixture()
        # set up functions for all test cases
       def setup(self):
           self.url = "https://669b606a276e45187d354732.mockapi.io/demo"
           self.api = APIfuntions(self.url)

        # created test cases to verify the status code
       def test_api_status_code(self, setup):
           assert self.api.api_status_code() == 200

       # test case to verify fetch_data
       def test_api_data_fetch(self, setup):
           assert self.api.fetch_api_data() == TestData.mock_data

       # test case to verify the header data
       def test_fetch_header(self, setup):
           headers = self.api.fetch_header()
           assert headers['Server'] == 'Cowboy'

       # test case to verify the  insert data
       def test_insert_data(self, setup):
           data = {'name': 'lrobn'}
           assert self.api.insert_data(data) == True

       # test case to verify the delete data
       def test_delete_data_by_id(self, setup):
           assert self.api.delete_data(6) == True


