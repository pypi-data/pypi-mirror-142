#task_success_response.py
import simplejson as json

__all__ = ['TaskSuccessResponse']
class TaskSuccessResponse:
    def __init__(self, status, supplier_details,pdf_details,detail):
       self.status= status
       self.supplier_details=supplier_details
       self.pdf_details=pdf_details
       self.detail = detail
       self.success = {"status":self.status, "supplier_json":self.supplier_details,"pdf_json":self.pdf_details,"detail":self.detail}
       
    def __str__(self):
        return json.dumps({"success": self.success})