#!/usr/bin/python3
"""
ONIMAP port scanner
"""
from datetime import datetime as date
from sys import exc_info as err
from sys import argv as args
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, setdefaulttimeout, TCP_NODELAY, IPPROTO_TCP
from socket import create_connection

def helper():
    """
    Displays the help message
    """
    print("ONIMAP2")
    print("Usage: ./onimap [flag] [host]")
    print("host is an ip address or name")
    print("Available flags:")
    print("-r    specifies remote host")
    print("-h    displays help")
    print("-t    specifies a timeout value (in s)")
    print("-p    specifies ports to scan")
    print("-P    specifies a port range to scan")
    print("-aP    scans all ports")
    print("Example: ./onimap -t 0.2 -p 22,34,443,8080 -r somehost.com")
    quit()

def main(targ, timeout, ports):
    """
    Main component of onimap
    @params:

        target:  - Required : ip/hostname of the scan (str)
        timeout: - Required : default socket time (float)
        ports:   - Required : array of ports to scan Array(int)
    """
    flag = False
    port_opens = "Onimap2 results:\nPORT\t| STATUS\n"
    print("="*30)
    print("ONIMAP2")
    print("Scanning target: "+targ)
    print("Time started: "+str(date.now()))
    print("="*30)
    try:
        print_progress_bar(0, len(ports), prefix='Progress:',
                         suffix='Complete')
        for port in ports:
            try:
                sock = socket(AF_INET, SOCK_STREAM)
                sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
                setdefaulttimeout(timeout)
                r = sock.connect_ex((targ,port))
                if r == 0:
                    flag = True
                    port_opens += "{}\t| open\n".format(port)
                    print_progress_bar(ports.index(port), len(ports), prefix='Progress:',
                                     suffix='Complete')
            except ConnectionError:
                pass
            except TimeoutError:
                pass
            except:
                pass
            finally:
                sock.close()
    except:
        print(err())
    print_progress_bar(len(ports), len(ports), prefix='Progress:',
                       suffix='Complete')
    if flag:
        print(port_opens)
    else:
        print("\n[!!!] - No open ports found")

def print_progress_bar(iteration, total, prefix='', suffix=''):
    """
    Call in a loop to create terminal progress bar
    \n@params:\n
        iteration   - Required  : current iteration (int)
        total       - Required  : total iterations (int)
        prefix      - Optional  : prefix string (str)
        suffix      - Optional  : suffix string (str)
        decimals    - Optional  : positive number of decimals (int)
        length      - Optional  : character length of bar (int)
        fill        - Optional  : bar fill character (str)
        printEnd    - Optional  : end character (e.g. "\\r", "\\r\\n") (str)
    """
    decimals = 1
    length = 40
    fill = '█'
    print_end = "\r"
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filled_length = int(length * iteration // total)
    outputbar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{outputbar}| {percent}% {suffix}', end=print_end)
    # Print New Line on Complete
    if iteration == total:
        print()

if __name__ == '__main__':
    TIMEOUT, HELP, PORTS, APORT = False, False, False, False
    TIMEOUT_VALUE = 10
    PORTS_VALUE = [20, 21, 22, 23, 25, 53, 67,
                   68, 80, 110, 143, 443, 3389, 8000, 8080]
    try:
        if "-t" in args:
            TIMEOUT = True
            TIMEOUT_VALUE = args[args.index("-t")+1]
            args.remove(TIMEOUT_VALUE)
            args.remove("-t")
        if "-h" in args:
            HELP = True
            args.remove("-h")
        if "-p" in args:
            PORTS = True
            PORTS_VALUE = [int(i) for i in args[args.index("-p")+1].split(",")]
        if "-P" in args:
            PORTS = True
            temp = [int(i) for i in args[args.index("-P")+1].split(",")]
            #PORTS_VALUE = [i for i in range(temp[0], temp[1]+1)]
            PORTS_VALUE = list(range(temp[0], temp[1]))
        if "-aP" in args:
            APORT = True
            PORTS_VALUE = list(range(0, 65536))
        if not "-r" in args:
            helper()
    except IndexError:
        helper()


    if HELP or (PORTS and APORT):
        helper()
    else:
        try:
            target = args[args.index("-r")+1]
        except IndexError:
            helper()
        main(target, float(TIMEOUT_VALUE), PORTS_VALUE)
