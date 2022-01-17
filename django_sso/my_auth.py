from .sessionfw import DaoInterface
import os
from libraries.sso import TwitterClass
from django.template import Context
from django.shortcuts import render
import secrets

def sso_login():
    
    tw = TwitterClass()

    auth_url = tw.get_authenticate_endpoint()

    return auth_url
    

def sso_callback(func):
    def inner(*args, **kwargs):
        
        tw = TwitterClass()
        f = func(*args, **kwargs)
        
        try:
            oauth_token = args[0].GET['oauth_token']
            oauth_verifier = args[0].GET['oauth_verifier']

            user = tw.get_auth_info(
                oauth_token,
                oauth_verifier,
            )

            userid = user['user_id']
            screenname = user['screen_name']
            
            # create a token
            token = secrets.token_hex(16)
            
            # create an instance for a session
            u = DaoInterface(token)
            # set onto the redis with user_id and screen_nam
            u.add_user(screenname, userid)
            u.save()

            # return cookie
            print(f)
            f.set_cookie(key="sessionkey", 
                value=token, 
                httponly=True,
                samesite='Lax'
            )

            return f

        except KeyError:
            pass

        return f
    return inner

def sso_auth_required(func):

    def inner(*args, **kwargs):

        sessionkey = args[0].COOKIES['sessionkey']
        # check the session on redis
        u = DaoInterface(sessionkey)
        try:
            print(u.all_data())
            
            # else if there is a session
            # provide the user infomation

            # extend time
            args[0].AUTH_STATE = True
            # get info from redis
            args[0].AUTH_INFO = True
            args[0].SESSIONKEY = sessionkey

            # if info is not on db
            # use twitterAPI to get info

            r = func(*args, **kwargs)

        except KeyError:
            # if the return is empty            
            # redirect to the login page(env)
            args[0].AUTH_STATE = False
            r = func(*args, **kwargs)
        return r
    return inner