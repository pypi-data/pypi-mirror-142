# job_number_constants.py

class JobNumberConstants:
    
    # Constants related to the project specific
    job_number_filter = "X-TaskList-JobNumber-Filters"
    get_sql_query = """
                    EXEC [CES].[sp_Get_Tasklist_JobNumber_UI]
                    @Exam_SR_Key = ?
                    """
    post_sql_query = """
                    EXEC [CES].[sp_Save_Tasklist_JobNumber_UI]
                    @Input_JSON = ?
                    """
    job_number_func = "jobNumber"
    job_number_func_val = "func:jobNumber"
    exam_key = "examKey"
    param_failure = "examKey query parameter is missing."
    input_json = "Input_JSON"
    exam_key_param = "Exam_SR_Key"