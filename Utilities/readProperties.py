import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class Readconfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def getUsername():
        user_name = config.get('common info', 'user_name')
        return user_name

    @staticmethod
    def getPassword():
        pwd = config.get('common info', 'password')
        return pwd

    @staticmethod
    def getWorkflowName():
        work_flow = config.get('common info', 'workflow_name')
        return work_flow

    @staticmethod
    def getDescription():
        workflow_desc = config.get('common info', 'workflow_description')
        return workflow_desc

    @staticmethod
    def getStatus1():
        status_name_first = config.get('common info', 'status1')
        return status_name_first

    @staticmethod
    def getStatus2():
        status_name_second = config.get('common info', 'status2')
        return status_name_second

    @staticmethod
    def getStatus3():
        third_successor = config.get('common info', 'status3')
        return third_successor

    @staticmethod
    def getStatus4():
        fourth_successor = config.get('common info', 'status4')
        return fourth_successor

    @staticmethod
    def getFormname():
        form_name = config.get('common info', 'hire_form_name')
        return form_name

    @staticmethod
    def getFormdescription():
        form_description = config.get('common info', 'hire_form_description')
        return form_description

    @staticmethod
    def getRequestgroupname():
        request_group = config.get('common info', 'request_group_name')
        return request_group

    @staticmethod
    def getGroupdescription():
        group_description = config.get('common info','request_description')
        return group_description

    @staticmethod
    def getRequestTypename():
        request_type = config.get('common info', 'request_type_name')
        return request_type

    @staticmethod
    def getRequestTypeDescription():
        request_type_description = config.get('common info', 'request_type_description')
        return request_type_description

