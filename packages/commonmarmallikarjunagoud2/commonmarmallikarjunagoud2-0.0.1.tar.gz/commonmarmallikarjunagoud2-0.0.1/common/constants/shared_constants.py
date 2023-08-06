#shared_constants.py

__all__ = ['SharedConstants']
class SharedConstants:

    """
    Common contants across packages and Web APIs

    """
    sql_connection_string = "SQL_CONNECTION_STRING"
    sql_copt_ss_access_token =1256
    request_val_failure = "Invalid Request"
    request_header_failure = "Header/Param validation failure"
    schema = "schema"
    bad_json_request_msg = "Invalid input, expected value"
    invalid_input_value_msg ="Invalid input"
    json_mime_type = "application/json"
    trace_enabled = "Trace_Enabled"
    response = "sp response"
    userId = "userId"
    main = '__main__'
    file_read_mode = 'r'
    method_type_get = "GET"
    date_format = "%d/%m/%Y"
    colon = ":"
    comma =","
    # _sql_copt_ss_access_token_value = 1256
   
