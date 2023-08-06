#AppStatus.py
import json

__all__ = ['ErrorResponse']
class ErrorResponse:
    def __init__(self, types, title, status, detail, instance):
       self.type = types
       self.title = title
       self.status= status
       self.detail = detail
       self.instance = instance
       self.error = {"types":self.type, "title": self.title, "status":self.status, "detail":self.detail, "instance": self.instance}
       
    def __str__(self):
        return json.dumps({"error": self.error})


