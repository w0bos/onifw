from os import getpid

import multiprocessing

sessions = {}


def save_current_session():
    """
    Saves the current session in a dicitonary
    """
    current_pid = getpid()
    current_id = len(sessions.keys())+1
    sessions[current_id]=current_pid


def delete_session(sessionid):
    """
    Delete the specified session
    \nArguments:\n
    sessionid : Required (int)
    """
    try:
        del sessions[sessionid]
    except:
        print("[!] - Unable to delete session {}".format(sessionid))

def session_switch(sessionid):
    """
    Switch to a specific session
    \nArguments:\n
    sessionid : Required (int)
    """

