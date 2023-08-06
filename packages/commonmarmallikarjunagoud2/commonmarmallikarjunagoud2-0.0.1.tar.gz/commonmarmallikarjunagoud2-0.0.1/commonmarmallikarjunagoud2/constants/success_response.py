#success_response.py
import simplejson as json

__all__ = ['SuccessResponse']
class SuccessResponse:
    def __init__(self, status, detail):
       self.status= status
       self.detail = detail
       self.success = {"status":self.status, "detail":self.detail}
       
    def __str__(self):
        return json.dumps({"success": self.success})