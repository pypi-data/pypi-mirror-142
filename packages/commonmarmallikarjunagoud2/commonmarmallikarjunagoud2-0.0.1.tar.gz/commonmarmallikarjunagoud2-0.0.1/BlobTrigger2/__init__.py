import logging

import azure.functions as func
import json
from common import SqlOperation, Logger, JsonHelper,ValidationHelper,CustomLog, AppStatus, SharedConstants
import requests

def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    sql_get_query = """
                        EXEC [CES].[sp_Get_File_Process_Test_DS]
                        @FILE_NAME = ?
                           """
    
    sql_save_query = """
                        EXEC [CES].[sp_Save_File_Process_Test_DS]
                        @FILE_NAME = ?, @INITIAL_FILE_COUNT= ?, @CURRENT_FILE_COUNT = ?, @ISNEW = ?
                           """
    param = myblob.name
    foldername = myblob.name.split('/')[1].split('.')[0]
    if foldername == 'ces' :
        filename = myblob.name.split('/')[2].split('.')[0]
        if filename.split('_').__len__() == 5:
            filenamear = filename.split('.')[0].split('_')
            filename = filenamear[0]+ '_' + filenamear[1] + '_'  + filenamear[2] + '_'  + filenamear[3]
        json_string = SqlOperation().fetch_one(sql_get_query, filename)
        #r=json.loads(json_string[0])['file_report']
        json_data = json.loads(json_string[0])['file_report']
        if json_data != None:
            json_data = json_data[0]
            if filename.__contains__(json_data['FILENAME']):
                if int(json_data['CURRENT_FILE_COUNT'])+1 == json_data['INITIAL_FILE_COUNT']:
                    blob_sas_uri = 'https://viruscantest09998d7354sa.blob.core.windows.net/clean-files/ces/'+filename+'.txt'+'?sp=racwl&st=2022-03-15T17:35:02Z&se=2022-03-16T01:35:02Z&spr=https&sv=2020-08-04&sr=c&sig=gWSeS6Oii1L6mHj1Ro06KV%2FVBakoS1%2Fm%2Fj7YvOxkVTM%3D'
                    headers = {
                        'x-ms-blob-type': 'BlockBlob'
                    }
                    r = requests.put(blob_sas_uri, headers=headers, data='success')

                    logging.info('all files scaned')
                else:
                    params = filename, json_data['INITIAL_FILE_COUNT'], int(json_data['CURRENT_FILE_COUNT'])+1, 'N'
                    json_string = SqlOperation().fetch_one(sql_save_query, params)





