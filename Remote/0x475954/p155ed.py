import paramiko, urllib, sys
import networkx as nx
import numpy as np


def ssh_auto_execute(ip_addr):
    ssh = paramiko.SSHClient()
    ssh.connect(hostname=ip_addr, port=22, timeout=2)
    cmd = "ls"
    stdin, stdout, stderr = ssh.exec_command(cmd)
    for line in stdout.readlines():
        print(line)
    ssh.close()


