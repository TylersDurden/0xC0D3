import urllib
import os, sys


def git_push():
    os.system('git status')
    os.system('git commit -m "Automated Commit"')
    os.system('git push origin')


def get_repo_root(user, repo):
    repo = repo+'/master/root.txt'
    uri = 'https://raw.githubusercontent.com/' + user + '/' + repo
    return urllib.urlopen(uri).read()


def parse_root(gitroot, verbose):
    root = {}
    files = []
    dirs = []
    for entry in gitroot.split('\n'):
        if len(entry.split('.')) == 2:
            files.append(entry)
        elif entry != '':
            dirs.append(entry)
    if verbose:
        print "Files: " + str(files)
        print "Dirs: " + str(dirs)
    root['files'] = files
    root['dirs'] = dirs
    return root


def main():
    if 'p' in sys.argv:
        git_push()

    git_root_node = parse_root(get_repo_root('TylersDurden', 'Base'), False)



if __name__ == '__main__':
    main()
