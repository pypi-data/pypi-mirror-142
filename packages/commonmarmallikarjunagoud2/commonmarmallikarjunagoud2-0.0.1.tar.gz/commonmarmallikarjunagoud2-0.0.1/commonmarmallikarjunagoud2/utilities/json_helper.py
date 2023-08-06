"""JSON HELPER CLASS """
import simplejson as json
from collections import namedtuple

__all__ = ['JsonHelper']
class JsonHelper:
        
    @staticmethod
    def parse_json(_json_string):
        """
        function to convert json string to json object
        """
        try:
        
           if _json_string is None:
              return (False,str({}))
           else:   
              json_data = json.loads(_json_string)
              return (True,json_data)
        
        except ValueError as ex:

           return (False,'Invalid json ' + str(ex))

    @staticmethod
    def parse_json_object(_json_string):
        """
        function to convert json string to json object
        """
        try:
        
           if _json_string is None:
              return (False,str({}))
           else:   
              json_data = json.loads(_json_string, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
              return (True,json_data)
        
        except ValueError:

           return (False,json_data)      

        

    @staticmethod
    def stringify_json(_json_data):
        """
        function to convert json object to string
        """
        try:

           json_string = json.dumps(_json_data, separators = (',',':'))
        
        except ValueError:

           return (False,json_string)

        return (True,json_string)



