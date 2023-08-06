#token_descriptor.py
import os
import requests
import struct
import sys
import logging


__all__ = ['TokenDescriptor']

identity_endpoint = os.environ["IDENTITY_ENDPOINT"]
identity_header = os.environ["IDENTITY_HEADER"] 
resource_uri= os.environ['SQL_RESOURCE_URI']
managed_id_client_id = os.environ["MANAGED_IDENTITY_CLIENT_ID"]
token_auth_uri = f"{identity_endpoint}?resource={resource_uri}&api-version=2019-08-01&client_id={managed_id_client_id}"
head_msi = {'X-IDENTITY-HEADER':identity_header}

class TokenDescriptor:
    # def __get__(self, instance, owner_class):
    #     try:
    #         self.auth = OAuth()
    #         token = self.auth.build_token_struct(self.auth.get_token(os.environ['SQL_RESOURCE_URI']))
    #         return token
    #     except:
    #         retmsg = 'Error - Error Info :' +  str(sys.exc_info()) 
    #         logging.error(f"{retmsg}")
    def __get__(self, instance, owner_class):
        resp = requests.get(token_auth_uri, headers=head_msi)
        access_token = resp.json()['access_token']
        accessToken = bytes(access_token, 'utf-8')
        exptoken = b""
        for i in accessToken:
                exptoken += bytes({i})
                exptoken += bytes(1)
        tokenstruct = struct.pack("=i", len(exptoken)) + exptoken
        return tokenstruct