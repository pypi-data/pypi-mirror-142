import jsonschema

__all__= ['ValidationHelper']
class ValidationHelper:

    @staticmethod
    def validate_json(_json_data,_json_schema):
        """
        function to validate Schema
        """
        jsonschema.Draft7Validator.check_schema(_json_schema)
        validator = jsonschema.Draft7Validator(_json_schema)
        validation_errors = sorted(validator.iter_errors(_json_data), key=lambda e: e.path)
        errors = []
        for error in validation_errors:
            message = error.message
            if error.path:
                message = "[{}] {}".format(
                    ".".join(str(x) for x in error.absolute_path), message
                )

            errors.append(message)
        return (len(errors) > 0 , errors)