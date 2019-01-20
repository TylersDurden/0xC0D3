import sys, os, time

highlight = '\33[43m'
red = '\33[91m'
blue = '\33[34m'
yellow = '\33[33m'
end = '\33[0m'
bold = '\33[1m'


class Sherlock:

    @staticmethod
    def find_cFiles():
        cmd = 'p=$PWD;cd /; find -name *.c >> cprogs.txt;  ' \
              'mv cprogs.txt $p; cd $p'
        os.system(cmd)
        c_programs = swap('cprogs.txt')
        print bold + "Found " + red + str(len(c_programs)) + end + \
              bold + blue + " Programs written in C" + end
        return c_programs

    @staticmethod
    def find_cplusplus():
        cmd = 'p=$PWD; cd /; find -name *.cpp'
        os.system(cmd + ' >> cpprogs.txt; mv cpprogs.txt $p; cd $p')
        cpp_progs = swap('cpprogs.txt')
        print bold + "Found " + red + str(len(cpp_progs)) + end + \
              bold + blue + " Programs written in C++" + end
        return cpp_progs

    @staticmethod
    def find_scripts():
        cmd = 'p=$PWD; cd /; find -name *.sh'
        os.system(cmd + ' >> scripts.txt; mv scripts.txt $p; cd $p')
        shells = swap('scripts.txt')
        print bold + "Found " + red + str(len(shells)) + end + \
              bold + blue + " Programs written in bash" + end
        return shells

    @staticmethod
    def find_volumes():
        os.system('lsblk>> vols.txt')
        media = swap('vols.txt')
        devs = list()
        for ln in media:
            # Try to find a partition
            try:
                devs.append(ln.split('part ')[1])
            except IndexError:
                pass
            try:
                devs.append(ln.split('crypt ')[1])
            except IndexError:
                pass
        print str(len(devs))+ " Mounted volumes/file systems identified"
        return devs


def swap(fname):
    data = list()
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n',''))
    os.system('rm '+fname)
    return data


def dir_ivy():
    print blue + '\33[32m' + "Top Dir. Contents: " + end
    os.system('ls />> top.txt')
    TOP = swap('top.txt')
    print str(len(TOP)) + " Directories in Top Level '/'"

    cmd = 'ls | while read element; do echo $element; done'
    for d in TOP:
        next_level = list()
        print highlight + bold + " Exploring /" + d + " " + end + red + bold
        try:
            os.system('cd /' + d + ';' + cmd + '>> levels.txt;cat levels.txt')
            levels = swap('levels.txt')
            print end
        except:
            pass
        time.sleep(1)
        print str(len(levels))+" Levels in "+d
        os.system('clear')
    return TOP


def main():
    start = time.time()
    CPrograms = Sherlock.find_cFiles()
    CppPrograms = Sherlock.find_cplusplus()
    shell_scripts = Sherlock.find_scripts()
    volumes = Sherlock.find_volumes()
    for vol in volumes:
        print '# '+vol
    dt = time.time() - start
    print blue+bold+str(dt)+end+bold+" Seconds Elapsed"+end

    time.sleep(3)
    os.system('clear')
    print "Phase Two: FileSystem Crawler"
    dir_ivy()


if __name__ == '__main__':
    main()

