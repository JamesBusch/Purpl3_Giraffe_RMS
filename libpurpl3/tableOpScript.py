import datetime
import libpurpl3.preferences as pref 
import libpurpl3.tableOp as tableOp
import libpurpl3.sqlFuncs as sqlFuncs
import sqlite3



class Script(tableOp.Entry):
    #TODO add default values
    # overriding abstract method
    def __init__(self, id: int, name: str, fileName: str, author: int, desc: str, dtCreated: datetime.datetime,
                 dtModified: datetime.datetime, size: float, isAdmin: bool):
        self.id = id
        self.name = name
        self.fileName = fileName
        self.author = author
        self.desc = desc
        self.dtCreated = dtCreated
        self.dtModified = dtModified
        self.size = size
        self.isAdmin = isAdmin

    # overriding abstract method
    def toJson(self):
        return {
            "id": str(self.id),
            "name": str(self.name),
            "fileName": str(self.fileName),
            "author": str(self.author),
            "desc": str(self.desc),
            "dtCreated": str(self.dtCreated),
            "dtModified": str(self.dtModified),
            "size": str(self.size),
            "isAdmin": str(self.isAdmin)
        }


class ScriptTable(tableOp.Table):
    # overriding abstract method
    @staticmethod
    def createTable():
        '''
        creates an empty SQL table for scripts
        @param None.
        @return errorCode: Error
        '''
        command = """CREATE TABLE IF NOT EXISTS s (
                       id INTEGER,
                       name CHAR(256),
                       fileName CHAR(256),
                       author INTEGER,
                       desc CHAR(1024),
                       dtCreated DATETIME.
                       dtModified DATETIME,
                       size FLOAT(5, 3),
                       isAdmin BOOL,
                       PRIMARY KEY(id),
                       FOREIGN KEY (author) REFERENCES u(id)
                    );"""
        e = sqlFuncs.createTable(command)
        return e

    # overriding abstract method
    @staticmethod 
    def getByID(id: int):
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        skelScript = Script(id, "SkeletonScriptName", "SkeletonScriptName.py", 1, "Skeleton Script Description", datetime.datetime.now(), datetime.datetime.now(), 0, False)
        return pref.getError(pref.ERROR_SUCCESS), skelScript

    # overriding abstract method
    @staticmethod
    def getAll():
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        skelScript1 = Script(1, "SkeletonScriptName1", "SkeletonScriptName1.py", 1, "Skeleton Script Description 1", datetime.datetime.now(), datetime.datetime.now(), 0, False)
        skelScript2 = Script(2, "SkeletonScriptName2", "SkeletonScriptName2.py", 1, "Skeleton Script Description 2", datetime.datetime.now(), datetime.datetime.now(), 0, False)
        scriptTup = (skelScript1, skelScript2)
        return pref.getError(pref.ERROR_SUCCESS), scriptTup

    # overriding abstract method
    @staticmethod
    def createEntry(values: tuple):
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        #TODO error check what is passed to function (in terms of types?)
        skelScript = Script(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8])
        return pref.getError(pref.ERROR_SUCCESS), skelScript

    # overriding abstract method
    @staticmethod
    def getAttrByID(attr: str, id: int):
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        # int
        if(attr == "id" or attr == "author"):
            return pref.getError(pref.ERROR_SUCCESS), 0
        #str
        elif(attr == "name" or attr == "fileName" or attr == "desc"):
            return pref.getError(pref.ERROR_SUCCESS), ""
        # datetime
        elif(attr == "dtCreated" or attr == "dtModified"):
            return pref.getError(pref.ERROR_SUCCESS), datetime.datetime.now()
        #float
        elif(attr == "size"):
            return pref.getError(pref.ERROR_SUCCESS), 0
        #bool
        elif(attr == "isAdmin"):
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
        skelScript = Script(0, "SkeletonScriptName", "SkeletonScriptName.py", 1, "Skeleton Script Description", datetime.datetime.now(), datetime.datetime.now(), 0, False)
        return pref.getError(pref.ERROR_SUCCESS), skelScript

    # overriding abstract method
    @staticmethod
    def add(entry: Script):
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        id: int = 0
        return pref.getError(pref.ERROR_SUCCESS), id
        

    # overriding abstract method
    @staticmethod
    def delete(id: int):
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
        skelScript = Script(0, "SkeletonScriptName", "SkeletonScriptName.py", 1, "Skeleton Script Description", datetime.datetime.now(), datetime.datetime.now(), 0, False)
        return pref.getError(pref.ERROR_SUCCESS), skelScript


