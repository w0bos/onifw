import core.confighandler as cfg
from core.gui import color
from os.path import dirname, abspath

installDir = dirname(abspath(__file__)) + '/../'
class ErrorHandler:

    def __init__(self,err, expected=False, retry=False):
        self.expected = expected
        self.retry = retry
        self.err = err
        self.err_string = "[!] - "
        self.string_manager()
    
    def string_manager(self):
        if self.expected == True:
            self.err_string += "An expected error occurred. "
        else:
            self.err_string += "An unexpected error occurred. "
        
        if self.retry == True:
            self.err_string += "Please retry."
        self.color_manager()
        self.display()

    def color_manager(self):
        self.err_string = color.WARNING + self.err_string + color.END
    
    def display(self):
        print(self.err_string)
        if cfg.check_value(installDir, "debug", False):
            print(color.LOGGING + str(self.err) + color.END)
