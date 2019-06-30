class ExampleDatabaseRouter(object):

    def db_for_read(self, model, **hints):
        # print(model.__name__)
        if model.__name__ == "Balance" or model.__name__ == "User" or model.__name__ == "Session":
            # print("read use default")
            return 'default'
        elif model.__name__ in ["Test", "Question", "Text", "Subject", "SubjectWithEightAnswer", "Test","Testt","ForCheck","SubjectWithTexts","PassedTest","History"]:
            # print("read use test")
            return "tests"
        return None

    def db_for_write(self, model, **hints):
        if model.__name__ == "Balance" or model.__name__ == "User" or model.__name__ == "Session":
            # print("write use default")
            return 'default'
        elif model.__name__ in ["Test","Question","Text","Subject","SubjectWithEightAnswer","Test","Testt","ForCheck","SubjectWithTexts","PassedTest","History"]:
            # print("write use test")
            return "tests"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        list=('default','tests')
        if obj1._state.db in list and obj2._state.db in list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'mainapp':
            return db == 'tests'
        elif db == 'tests':
            return False
        return None



