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