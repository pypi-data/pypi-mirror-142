import os
import sys
sys.path.insert(0, os.getcwd())

class EnvironmentVariable:

    def __init__(self):
        os.environ['IDENTITY_ENDPOINT'] =''
        os.environ['IDENTITY_HEADER'] =''
        os.environ['Trace_Enabled'] =''
        os.environ['SQL_DB'] =''
        os.environ['SQL_CONNECTION_STRING'] = ''
        os.environ['SQL_RESOURCE_URI'] =''
        os.environ['MANAGED_IDENTITY_CLIENT_ID'] =''
        os.environ['SQL_DRIVER'] =''
        os.environ['SQL_SERVER'] =''
        os.environ['APPINSIGHTS_INSTRUMENTATIONKEY'] ='b4c9a07a-d78f-43cd-ad26-b1426011edc7'