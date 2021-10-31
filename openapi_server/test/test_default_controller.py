# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_music_api_artist_post(self):
        """Test case for music_api_artist_post

        retrieves a list of artists or list of album releases if only one artist matched
        """
        body = {"artist":{"name":"Pink Floyd","id":"83d91898-7763-47d7-b03b-b92132375c47"}}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/music-api/artist',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
