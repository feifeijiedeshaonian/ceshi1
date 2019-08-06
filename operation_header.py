from operation_json import OperationJson


class OperationHeader:

    def write_token(self, response):
        op_json = OperationJson()
        op_json.write_data(response)