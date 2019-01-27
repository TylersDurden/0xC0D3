import os, sys, utility


class PointToMe:

    data_list = []
    data_str = ''
    data_int = 0
    types = ['list', 'str', 'int']
    reference = {'list': data_list,
                 'str': data_str,
                 'int': data_int}

    def __init__(self, data, type):
        if type in self.types:
            if type=='int':
                self.data_int = data
            if type == 'str':
                self.data_str = data


if '-read' in sys.argv:
    path_to_data = sys.argv[2]
    # data = utility.swap(path_to_data, "True")
    print PointToMe(path_to_data, int).data_int


def log_process_memory_location(data, log_file):
    for line in data:
        open(log_file, 'a').write(line+'\n')


def get_stack_mem_pointer(location):
    data = {}
    pointer = location.pop().split("=")[1]
    contents = location.pop().split("=")[1]
    data[pointer] = contents
    print data
    return data


def main():
    if 'buggy_0' in sys.argv:
        print utility.execute('python p4x.py -read 420', True)
    if 'overfloweth' in sys.argv:
        print PointToMe(sys.argv[2], 'int')
    if 'stacksmash' in sys.argv:
        stack = []
        if len(sys.argv) == 4:
            stack_depth = sys.argv[3]
        else:
            stack_depth = 20
        for i in range(int(sys.argv[2])):
            inner_pointer = utility.execute('sh sma.sh ' + str(stack_depth), True).pop().replace('>', '')
            stack.append(inner_pointer)
        for stack_pointer in stack:
            print str(os.system('printf %d ' + stack_pointer)) + " : " + stack_pointer
            process_memory_location = utility.execute('./m3m '+stack_pointer, True)
            log_process_memory_location(process_memory_location, 'log.txt')
            get_stack_mem_pointer(process_memory_location)
            os.system('rm log.txt')
            print '-----------------------------------------'


if __name__ == '__main__':
    main()
