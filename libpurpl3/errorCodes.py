'''
This file holds the definaion of all the error codes contained in
the applications. error codes should only be accessed by preferences manager
and never use hard coded values
errors with use the following format
ERROR:ENUM_NAME: Error(code,string)
To retrive errors use getError(str,args:Tuple = None) function
ex
  getError(pref.ERROR_UNKNOWN,args=(err))
  getError(pref.ERROR_SUCCESS)
'''


class Error():
  '''
  Error hold error code and string description of error
  use:
    getError(key: str,args:Tuple[Any] = None ) -> Tuple[Error, Any]
  to create errors
  ex
    getError(pref.ERROR_UNKNOWN,args=(err))
    getError(pref.ERROR_SUCCESS)
  '''
  code = None
  string = None
  extraVars = tuple()

  def __init__(self,code: int,string: str):
    self.code = code
    self.string = string

  def setExtraVars(self,*extraVars) -> None:
    '''
      @param extraVars any extra var that is needed when printing the Error
      Sets extra values used in the output of the error
      ex if setExtraVars("test") is passed and its an unknown error (code 1)
      first %d is always the error code and does not need to be passed.
        unknown_err.str = "Returned: %d, an unknown error has occurred: %s"
      it will become:
        Returned 1, an unknown error has occurred: test
    '''
    self.extraVars = extraVars

  def __str__(self):
    return self.string  % ((self.code,) + self.extraVars)

  def __eq__(self, other):
    return self.code == other.code


#Used so get attribute isn't need everytime to create return 0
Success = Error(0,"Returned: %d, no error has occurred.")

def getAttrName(attr: str) -> str:
  '''
  @param attr the attribute that will be parsed.
  @return the name of the attribute.
  Returns the name of the attribute / how it will be saved in the config
  file. each level of the config file is denoted by and ':' thus the last value will
  be the attr's name
  ie
    ERROR:UNKNOWN
  returns
    UNKNOWN
  '''
  return attr.split(":")[-1]


def getErrorCodeList() -> dict:
  '''Returns a dictionatry with all the error codes
  @return dict of all error codes. This should only be used
  by preferences.py
  '''
  return {
    #0-30
    getAttrName(ERROR_SUCCESS): Success,
    getAttrName(ERROR_UNKNOWN): Error(1,"Returned: %d, an unknown error has occurred: %s"),
    
    getAttrName(ERROR_FILE_NOT_FOUND): Error(3,"Returned: %d, file %s was not found"),
    
    getAttrName(ERROR_ATTRIBUTE_NOT_FOUND) : Error(20,"Returned: %d, Attribute %s could not be found.")
  }

#0-30
ERROR_SUCCESS = "ERROR:ERROR_SUCCESS"
ERROR_UNKNOWN = "ERROR:ERROR_UNKNOWN"

ERROR_FILE_NOT_FOUND = "ERROR:FILE_NOT_FOUND"

ERROR_ATTRIBUTE_NOT_FOUND = "ERROR:ATTRIBUTE_NOT_FOUND"