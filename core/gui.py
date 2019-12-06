import random
class color:
    #Rename
    HEADER      =   '\033[96m'
    IMPORTANT   =   '\033[35m'
    NOTICE      =   '\033[32m'
    OKBLUE      =   '\033[94m'
    OKGREEN     =   '\033[92m'
    WARNING     =   '\033[91m'
    RED         =   '\033[31m'
    END         =   '\033[0m'
    LOGGING     =   '\033[93m'
    WHITE       =   '\033[97m'
    #Text formatting
    BOLD        =   '\033[1m'
    UNDER       =   '\033[4m'

    color_random = [HEADER, IMPORTANT, NOTICE, OKBLUE, OKGREEN, WARNING, RED, LOGGING]
    random.shuffle(color_random)
