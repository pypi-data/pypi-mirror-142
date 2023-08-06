#response_message.py
__all__ = ['CustomMessage']
class CustomMessage:
    """Constants for response message
    """
    bad_request = f'Bad Request'

    internal_server_error = f'There is a problem with the resource you are looking for- please connect with admin'

    not_acceptable =f'Not Acceptable'
    
    no_content = f' No Content found'
