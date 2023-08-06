#Logger.py


import os
from applicationinsights import TelemetryClient
from ..patterns import Singleton

__all__ = ['Logger']

class Logger(metaclass = Singleton):
    # tele_client = TelemetryClient('b4c9a07a-d78f-43cd-ad26-b1426011edc7')
    app_insight_key = os.environ["APPINSIGHTS_INSTRUMENTATIONKEY"]
    tele_client = TelemetryClient(app_insight_key)
    tele_client.channel.sender.send_interval_in_milliseconds = 30 * 1000
    def __init__(self, **kwargs):
        """
        Initialize a new instance of the Logger class
        """
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'start_time' in kwargs:
            self.start_time = kwargs['start_time']

    def request(self, **kwargs ):
        """Sends a single request that was captured for the application.
 
        Args:
            name (str). the name for this request. All requests with the same name will be grouped together.\n
            url (str). the actual URL for this request (to show in individual request instances).\n
            success (bool). true if the request ended in success, false otherwise.\n
            start_time (str). the start time of the request. The value should look the same as the one returned by :func:`datetime.isoformat()` (defaults to: None)\n
            duration (int). the number of milliseconds that this request lasted. (defaults to: None)\n
            response_code (string). the response code that this request returned. (defaults to: None)\n
            http_method (string). the HTTP method that triggered this request. (defaults to: None)\n
            properties (dict). the set of custom properties the client wants attached to this data item. (defaults to: None)\n
            measurements (dict). the set of custom measurements the client wants to attach to this data item. (defaults to: None)
        """
        try:
            if "status" not in kwargs:
                self.status = True
            else:
                self.status = kwargs['status']
            if 'uri' not in kwargs:
                self.uri = None
            self.duration = 0
            self.response_code = None
            if 'http_method' not in kwargs:
                self.http_method = None
            else:
                self.http_method = kwargs['http_method']
            self.properties = kwargs['properties']

            Logger.tele_client.track_request(self.name, self.uri, self.status, self.start_time, self.duration, self.response_code, self.http_method, self.properties)
            
        finally:
            Logger.tele_client.flush()
    def exception(self, **kwargs):
        """ Send information about a single exception that occurred in the application.
 
        Args:
            type (Type). the type of the exception that was thrown.\n
            value (:class:`Exception`). the exception that the client wants to send.\n
            tb (:class:`Traceback`). the traceback information as returned by :func:`sys.exc_info`.\n
            properties (dict). the set of custom properties the client wants attached to this data item. (defaults to: None)\n
            measurements (dict). the set of custom measurements the client wants to attach to this data item. (defaults to: None)
        """
        try:

            self.properties = kwargs['properties']
            self.value = kwargs['value']
            self.tb = kwargs['tb']
            self.type = kwargs['type']
            Logger.tele_client.track_exception(self.type, self.value, self.tb, self.properties )
            
        finally:
            Logger.tele_client.flush()
        
    def trace(self,**kwargs):
        """Sends a single trace statement.
 
        Args:
            name (str). the trace statement.\n
            properties (dict). the set of custom properties the client wants attached to this data item. (defaults to: None)
        """
        try:

            self.properties = kwargs['properties']
            if 'severity' not in kwargs:
                self.severity = None
            else:
                self.severity = kwargs['severity']
            Logger.tele_client.track_trace(self.name, self.properties, self.severity)
        finally:
            Logger.tele_client.flush()

    def event(self, name, **kwargs):
        """ Send information about a single event that has occurred in the context of the application.
 
        Args:
            name (str). the data to associate to this event.\n
            properties (dict). the set of custom properties the client wants attached to this data item. (defaults to: None)\n
            measurements (dict). the set of custom measurements the client wants to attach to this data item. (defaults to: None)
        """
        try:
            self.properties = kwargs['properties']
            Logger.tele_client.track_event(self.name, self.properties)
        finally:
            Logger.tele_client.flush()

