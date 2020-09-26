import core.confighandler as cfg
from datetime import date

class LogHandler:
    def __init__(self, installDir, logDir, cmd=[], boot=False):
        self.logDir = logDir
        self.installDir = installDir
        self.logFile = self.logDir + "oni.log"
        self.log_status = cfg.check_value(installDir, "save_session", False)
        self.cmd = cmd
        if boot:
            self.write_boot()
        else:
            if self.log_status:
                if len(self.cmd) >= 1:
                    self.write_logs()

    def write_logs(self):
        with open(self.logFile, "a") as file_log:
            file_log.write("[input][{}] : ".format(
                date.today()) + ''.join(e + " " for e in self.cmd) + "\n")
        file_log.close()


    def handle_no_cmd(self):
        pass

    def write_boot(self):
        with open(self.logFile, "a") as file_log:
            file_log.write("[Starting onifw][{}]\n".format(date.today()))
        file_log.close()
