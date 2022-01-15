import os

from django.http import request
from requests_oauthlib import OAuth1Session
from urllib.parse import parse_qsl
from django.conf import settings


class TwitterClass:
    def __init__(self):
        self.tw_ck = settings.TW_CK
        self.tw_cs = settings.TW_CS
        self.authenticate_url = "https://api.twitter.com/oauth/authenticate"
        # domain of the website
        self.baseurl = settings.BASE_DOMAIN
    
    def get_authenticate_endpoint(self):
        twitter = OAuth1Session(self.tw_ck, self.tw_cs)
        url = 'https://api.twitter.com/oauth/request_token'
        oauth_callback = self.baseurl + settings.TW_AUTH_CALLBACK
        response = twitter.post(
            url,
            params = {'oauth_callback': oauth_callback}
        )
        
        request_token = (dict(parse_qsl(response.content.decode("utf-8"))))
        
        authenticate_endpoint = '%s?oauth_token=%s' \
            % (self.authenticate_url, request_token['oauth_token'])

        return authenticate_endpoint
    
    def get_auth_info(self, oauth_token, oauth_verifier):
        url = 'https://api.twitter.com/oauth/access_token'
        twitter = OAuth1Session(
            self.tw_ck,
            self.tw_cs,
            oauth_token,
            oauth_verifier,
        )

        response = twitter.post(
            url,
            params={'oauth_verifier': oauth_verifier}
        )

        auth_info = dict(parse_qsl(response.content.decode("utf-8")))

        return auth_info

