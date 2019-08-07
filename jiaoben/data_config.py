class GlobalBar:
    # case_id
    Id = "0"
    request_name = "1"
    url = "2"
    run = "3"
    requset_way = "4"
    token = "5"
    header = "6"
    header_1 = "7"
    case_depend = "8"
    data_depend = "9"
    field_depend = "10"
    data = "11"
    expext = "12"
    result = "13 "

    # 获取caseid
    def get_id():
        return GlobalBar.Id

    # 获取caseurl
    def get_url():
        return GlobalBar.url

    # 获取caserun
    def get_run():
        return GlobalBar.run

    # 获取caserequset_way
    def get_requset_way():
        return GlobalBar.requset_way

    # 获取casetoken
    def get_token():
        return GlobalBar.token

    # 获取caseheader
    def get_header():
        return GlobalBar.header

    # 获取casecase_depend
    def get_case_depend():
        return GlobalBar.case_depend

    # 获取casedata_depend
    def get_data_depend():
        return GlobalBar.data_depend

    # 获取casefield_depend
    def get_field_depend():
        return GlobalBar.field_depend

    # 获取casedata
    def get_data():
        return GlobalBar.data

    # 获取caseexpext
    def get_expect():
        return GlobalBar.expext

    # 获取caseresult
    def get_result():
        return GlobalBar.result

    def get_header_value():
        return GlobalBar.header_1