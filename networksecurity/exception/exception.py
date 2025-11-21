import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self,error,error_detail:sys):
        _,_,exc_tb=error_detail.exc_info()
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        def __self__(self):
            return "error in file [{0}] in the line [{1}] and the error is [{2}]".format(
                self.file_name,self.lineno,str(self.error))
if __name__=="__main__":
    try:
        logger.logging.info("entered exception block")
        a=1/0
    except Exception as e:
        raise NetworkSecurityException(e,sys)