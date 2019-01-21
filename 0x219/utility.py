import os


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def write(fname, data):
    f = open(fname, 'w')
    for buff in data:
        f.write(buff)


def execute(command, destroy):
    os.system(command+'>> command.txt')
    return swap('command.txt', destroy)


def list2str(words):
    str_out = ''
    for element in words:
        str_out += element
    return str_out


# #################### END OF UTILITY FILES #################### #
