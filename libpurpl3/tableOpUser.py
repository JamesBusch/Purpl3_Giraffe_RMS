import datetime
import libpurpl3.preferences as pref
import libpurpl3.tableOp as tableOp

class User(tableOp.Entry):
    #TODO add default values
    # overriding abstract method
    def __init__(self, ID: int, username: str, password: str, dtCreated: datetime.datetime,
                 dtModified: datetime.datetime, admin: bool):
        self.ID = ID
        self.username = username
        self.password = password
        self.dtCreated = dtCreated
        self.dtModified = dtModified
        self.admin = admin

    # overriding abstract method
    def toJson(self):
        return {
            "ID": str(self.ID),
            "username": str(self.username),
            "password": str(self.password),
            "dtCreated": str(self.dtCreated),
            "dtModified": str(self.dtModified),
            "admin": str(self.admin)
        }


class UserTable(tableOp.Table):
    # overriding abstract method
    @staticmethod
    def createTable():
        '''
        creates an empty SQL table for scripts
        @param None.
        @return errorCode: Error
        '''
        return pref.getError(pref.ERROR_SUCCESS)

    # overriding abstract method
    @staticmethod
    def getByID(ID: int):
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        skelUser = User(ID, "username", "hashed password", datetime.datetime.now(), datetime.datetime.now(), False)
        return pref.getError(pref.ERROR_SUCCESS), skelUser

    # overriding abstract method
    @staticmethod
    def getAll():
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        skelUser1 = User(0, "username1", "hashed password 1", datetime.datetime.now(), datetime.datetime.now(), False)
        skelUser2 = User(1, "username2", "hashed password 2", datetime.datetime.now(), datetime.datetime.now(), False)
        userTup = (skelUser1, skelUser2)
        return pref.getError(pref.ERROR_SUCCESS), userTup

    # overriding abstract method
    @staticmethod
    def createEntry(values: tuple):
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        # TODO error check what is passed to function (in terms of types?)
        skelUser = User(values[0], values[1], values[2], values[3], values[4], values[5])
        return pref.getError(pref.ERROR_SUCCESS), skelUser

    # overriding abstract method
    @staticmethod
    def getAttrByID(attr: str, ID: int):
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        # int
        if (attr == "ID"):
            return pref.getError(pref.ERROR_SUCCESS), 0
        # str
        elif (attr == "username" or attr == "password"):
            return pref.getError(pref.ERROR_SUCCESS), ""
        # datetime
        elif (attr == "dtCreated" or attr == "dtModified"):
            return pref.getError(pref.ERROR_SUCCESS), datetime.datetime.now()
        # bool
        elif (attr == "admin"):
            return pref.getError(pref.ERROR_SUCCESS), False
        else:
            return pref.getError(pref.ERROR_ATTRIBUTE_NOT_FOUND), None

    # overriding abstract method
    @staticmethod
    def getWithQuery(query: str):
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        skelUser = User(0, "username1", "hashed password 1", datetime.datetime.now(), datetime.datetime.now(), False)
        return pref.getError(pref.ERROR_SUCCESS), skelUser

    # overriding abstract method
    @staticmethod
    def add(entry: User):
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        ID: int = 0
        return pref.getError(pref.ERROR_SUCCESS), ID

    # overriding abstract method
    @staticmethod
    def delete(ID: int):
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        return pref.getError(pref.ERROR_SUCCESS)

    # overriding abstract method
    @staticmethod
    def editEntry(values: tuple):
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        skelUser = User(0, "username1", "hashed password 1", datetime.datetime.now(), datetime.datetime.now(), False)
        return pref.getError(pref.ERROR_SUCCESS), skelUser