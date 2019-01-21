import urllib
import os, sys


def git_push():
    os.system('git status')
    os.system('git commit -m "Automated Commit"')
    os.system('git push origin')


username = 'TylersDurden'
repo = 'Base/master/'
uri = 'https://raw.githubusercontent.com/'+username+'/'+repo
urllib.urlopen(uri)



if 'p' in  sys.argv:
    git_push()