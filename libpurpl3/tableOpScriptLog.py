import datetime
from datetime import datetime as dt
import libpurpl3.preferences as pref
import libpurpl3.tableOp as tableOp
import libpurpl3.sqlFuncs as sqlFuncs
import libpurpl3.tableOpScript as tos
import sqlite3

class ScriptLog(tableOp.Entry):
    # TODO add default values
    # overriding abstract method
    def __init__(self, ID: int, scriptID: int, userID: int, compID: int, startTime: datetime.datetime,
                endTime: datetime.datetime, returnVal: int, errorCode: int, stdoutFile: str, stderrFile: str,
                 asAdmin: bool):
        '''
        Creates scriptLog object. Contains all info on the execution of a given script on a given computer by a specific user.
        @param 
            ID: int - unique identifier automatically generated when scriptLog is added to sql table. Will be None until scriptLog is added to table.
            scriptID: int - primary key of script table to indicate which script was executed
            userID: int - primary key of user table to indicate which user executed script
            compID: int - primary key of computer table to indictae which computer is having script executed on it
            startTime: datetime.datetime - dateTime when createEntry is called for the scriptLog
            endTime: datetime.datetime - dateTime when createEntry script execution is finished
            returnVal: int - value returned from script execution 
            errorCode: int - error code returned from script execution
            stdoutFile: str - file location where stdout logs will be stored from script execution
            stderrFile: str - file location where stderr logs will be stored from script execution
            asAdmin: bool - whether or not the script was executed as admin
        @return 
            None.
        '''
        self.ID = ID
        self.scriptID = scriptID
        self.userID = userID
        self.compID = compID
        self.startTime = startTime
        self.endTime = endTime
        self.returnVal = returnVal
        self.errorCode = errorCode
        self.stdoutFile = stdoutFile
        self.stderrFile = stderrFile
        self.asAdmin = asAdmin

    # overriding abstract method
    def toJson(self):
        '''
        Returns a dictionary of all object attributes as strings.
        @param 
            None.
        @return
            Dictionary of all object attributes as strings.
        '''
        return {
            "ID": str(self.ID),
            "scriptID": str(self.scriptID),
            "userID": str(self.userID),
            "compID": str(self.compID),
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
        command = """CREATE TABLE IF NOT EXISTS sl (
                       id INTEGER PRIMARY KEY,
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
                       FOREIGN KEY (scriptId) REFERENCES s(id),
                       FOREIGN KEY (userId) REFERENCES u(id),
                       FOREIGN KEY (compId) REFERENCES c(id)
                    );"""
        # e = sqlFuncs.createTable(command, "ScriptLog")
        e = sqlFuncs.exeCommand(command, "createTable", "ScriptLog")
        return e

    # overriding abstract method
    @staticmethod
    def deleteTable():
        '''
        Removes the scriptLog SQL table from the database. Used for testing principally.
        @param None.
        @return e - Error code, returns success if no error occurs.
        '''
        command = """DROP TABLE sl;
                  """
        e = sqlFuncs.exeCommand(command, "deleteTable", "ScriptLog")
        return e

    # overriding abstract method
    @staticmethod
    def getByID(ID: int):
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        skelScriptLog = ScriptLog(ID, 0, 0, 0, datetime.datetime.now(), datetime.datetime.now(), 1, 1, "stdoutFile.txt",
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
    def createEntry(scriptID: int, userID: int, compID: int, asAdmin: bool):
        '''
        #TODO
        *add description*.
        @param *add param*.
        @return *add return*.
        '''
        # id will be set when object is added to table
        id = None
        # set startTime to "now"
        startTime = dt.now()
        # endTime, returnVal, errorCode are none - will be created through calls to editEntry
        endTime = None
        returnVal = None
        errorCode = None
        # create names/files for stdoutFile, stderrFile - {STDOUT/STDERR}_SCRIPT_ID.log requires scriptLog ID and thus must be done in add function
        stdoutFile = None
        stderrFile = None
        # create scriptLog object
        scriptLog = ScriptLog(id, scriptID, userID, compID, startTime, endTime, returnVal, errorCode, stdoutFile, stderrFile, asAdmin)
        return pref.getError(pref.ERROR_SUCCESS), scriptLog

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
        if (attr == "ID" or attr == "scriptID" or attr == "userID" or attr == "compID" or attr == "returnVal" or
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
        ID: int = 0
        stdoutFile = "STDOUT_" + str(tos.ScriptTable().getAttrByID("name", scriptID)) + "_" + str("FIXME") + ".log" # use 
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
        skelScriptLog = ScriptLog(0, 0, 0, 0, datetime.datetime.now(), datetime.datetime.now(), 1, 1, "stdoutFile1.txt",
                                  "stderrFile1.txt", False)
        return pref.getError(pref.ERROR_SUCCESS), skelScriptLog
