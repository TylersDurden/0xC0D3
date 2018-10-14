import sys, os

def usage():
    print "Incorrect Usage!"
    print "python privesc.py -mode arg"
    
def main():
   if len(sys.argv) < 3:
       usage()
   elif sys.argv[2] == '-prog':
       os.system('chmod +x '+ sys.argv[2])
   elif sys.argv[2] == 'root':
       os.system('sudo su')


if __name__ == '__main__':
    main()

