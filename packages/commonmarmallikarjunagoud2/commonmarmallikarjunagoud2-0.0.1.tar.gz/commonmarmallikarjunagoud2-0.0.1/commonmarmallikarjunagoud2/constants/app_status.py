#AppStatus.py

from enum import Enum

__all__ = ['AppStatus']

class AppStatus(Enum):
 
    bad_Request = (400, 'Bad Request')
    internal_server_error  = (500,'Internal Server Error')
    record_created = (201, 'Created')
    ok = ( 200, 'OK')
    no_content = (204, 'Not Acceptable')
    partial_content = (206, 'Partial Content')

    def __new__(cls, member_value, member_phrase):

        member = object.__new__(cls)
        member._value = member_value
        member.phrase = member_phrase
        
        return member


