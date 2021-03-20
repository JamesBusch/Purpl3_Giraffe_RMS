import datetime
import libpurpl3.preferences as pref
import libpurpl3.tableOp as tableOp
import sqlite3


class ScriptLog(tableOp.Entry):
    # TODO add default values
    # overriding abstract method
    def __init__(self, id: int, scriptId: int, userId: int, compId: int, startTime: datetime.datetime,
                endTime: datetime.datetime, returnVal: int, errorCode: int, stdoutFile: str, stderrFile: str,
                 asAdmin: bool):
        self.id = id
        self.scriptId = scriptId
        self.userId = userId
        self.compId = compId
        self.startTime = startTime
        self.endTime = endTime
        self.returnVal = returnVal
        self.errorCode = errorCode
        self.stdoutFile = stdoutFile
        self.stderrFile = stderrFile
        self.asAdmin = asAdmin

    # overriding abstract method
    def toJson(self):
        return {
            "id": str(self.id),
            "scriptId": str(self.scriptId),
            "userId": str(self.userId),
            "compId": str(self.compId),
            "startTime": str(self.startTime),
            "endTime": str(self.endTime),
            "returnVal": str(self.returnVal),
            "errorCode": str(self.errorCode),
            "stdoutFile": str(self.stdoutFile),
            "stderrFile": str(self.stderrFile),
            "asAdmin": str(self.asAdmin)
        }


class ScriptLogTable(tableOp.Table):
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
                       scriptId INTEGER,
                       userId INTEGER,
                       compId INTEGER,
                       startTime DATETIME,
                       endTime DATETIME,
                       returnVal INTEGER,
                       errorCode INTEGER,
                       stdoutFile CHAR(256),
                       stderrFile CHAR(256),
                       asAdmin BOOL,
                       PRIMARY KEY(id),
                       FOREIGN KEY (scriptId) REFERENCES s(id),
                       FOREIGN KEY (userId) REFERENCES u(id),
                       FOREIGN KEY (compId) REFERENCES c(id)
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
        skelScriptLog = ScriptLog(id, 0, 0, 0, datetime.datetime.now(), datetime.datetime.now(), 1, 1, "stdoutFile.txt",
                                  "stderrFile.txt", False)
        return pref.getError(pref.ERROR_SUCCESS), skelScriptLog

    # overriding abstract method
    @staticmethod
    def getAll():
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        skelScriptLog1 = ScriptLog(0, 0, 0, 0, datetime.datetime.now(), datetime.datetime.now(), 1, 1,
                                   "stdoutFile1.txt", "stderrFile1.txt", False)
        skelScriptLog2 = ScriptLog(1, 0, 0, 0, datetime.datetime.now(), datetime.datetime.now(), 1, 1,
                                   "stdoutFile2.txt", "stderrFile2.txt", False)
        scriptLogs = (skelScriptLog1, skelScriptLog2)
        return pref.getError(pref.ERROR_SUCCESS), scriptLogs

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
        skelScriptLog = ScriptLog(values[0], values[1], values[2], values[3], values[4], values[5], values[6],
                                  values[7], values[8], values[9], values[10])
        return pref.getError(pref.ERROR_SUCCESS), skelScriptLog

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
        if (attr == "id" or attr == "scriptId" or attr == "userId" or attr == "compId" or attr == "returnVal" or
                attr == "errorCode"):
            return pref.getError(pref.ERROR_SUCCESS), 0
        # str
        elif (attr == "stdoutFile" or attr == "stderrFile"):
            return pref.getError(pref.ERROR_SUCCESS), ""
        # datetime
        elif (attr == "startTime" or attr == "endTime"):
            return pref.getError(pref.ERROR_SUCCESS), datetime.datetime.now()
        # bool
        elif (attr == "asAdmin"):
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
        skelScriptLog = ScriptLog(0, 0, 0, 0, datetime.datetime.now(), datetime.datetime.now(), 1, 1, "stdoutFile1.txt",
                               "stderrFile1.txt", False)
        return pref.getError(pref.ERROR_SUCCESS), skelScriptLog

    # overriding abstract method
    @staticmethod
    def add(entry: ScriptLog):
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
        skelScriptLog = ScriptLog(0, 0, 0, 0, datetime.datetime.now(), datetime.datetime.now(), 1, 1, "stdoutFile1.txt",
                                  "stderrFile1.txt", False)
        return pref.getError(pref.ERROR_SUCCESS), skelScriptLog
