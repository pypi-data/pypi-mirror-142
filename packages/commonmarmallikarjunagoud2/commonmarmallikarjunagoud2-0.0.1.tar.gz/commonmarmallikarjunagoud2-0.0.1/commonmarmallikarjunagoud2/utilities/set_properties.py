#set_properties.py

import sys
import os
from common import CustomLog,SharedConstants
from datetime import datetime, timezone

__all__ = ['SetProperties']
class SetProperties:
   
   def __init__(self,name,value):
      """
      Initialize a request start time and class of the SetProperties class

      """
      self._properties = {name : value}
      self._properties[CustomLog.start_time] = datetime.now(timezone.utc).isoformat()
      self._properties[CustomLog.status] = True
   
   def sprequest_time(self):
      """
      SetProperties class to log the sp requested start time

      """   
      self._properties[CustomLog.sprequest_time] = datetime.now(timezone.utc).isoformat()
   
   def sprequest_params(self,sp_req_params):
      """
      SetProperties class to log the sp requested parameter

      """   
      self._properties[CustomLog.sp_req_param] = sp_req_params
   
   def sprequestend_time(self):
      """
      SetProperties class to log the sp requested end time

      """ 
      self._properties[CustomLog.sprequestend_time] = datetime.now(timezone.utc).isoformat()

   def end_time(self):
      """
      Initialize a request end time  of the SetProperties class

      """ 
      self._properties[CustomLog.end_time] = datetime.now(timezone.utc).isoformat()
   
   def error_messsage(self,message):
      """
      SetProperties class for initializa a error message

      """ 
      self._properties[CustomLog.error_messsage] = message

   def status(self,status):
      """
      SetProperties class for initializa a status

      """ 
      self._properties[CustomLog.status] = status
      
        