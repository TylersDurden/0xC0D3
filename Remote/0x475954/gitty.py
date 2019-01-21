import urllib
import os, sys


class GIT:

    api_uri = 'https://api.github.com'
    user_name = ''
    user_data = {}
    verbose = False

    def __init__(self, user, verbosity):
        self.user_name = user
        self.verbose = verbosity
        self.user_data = self.check_user_exists()
        self.user_data['repo_list'] = self.pull_user_repository_list()
        self.user_data['follower_data'] = self.get_user_followers()

    def set_verbosity(self, is_verbose):
        self.verbose = is_verbose

    def check_user_exists(self):
        user_data = {}
        is_real = False
        uri = self.api_uri+'/search/users?q='+self.user_name
        is_user = urllib.urlopen(uri).read()
        for entry in is_user.split('":"'):
            try:
                found = entry.split('"total_count":')[1].split(',"')[0]
                print "\033[1mFound "+found+" User(s) with name \033[35m"+self.user_name+'\033[0m'
                is_real = True
            except IndexError:
                pass
        if is_real:
            user_info = is_user.split('items":[')[1].split("]")[0]
            for data in user_info.split(','):
                try:
                    user_data['login'] = data.split('"login":')[1]
                except IndexError:
                    pass
                try:
                    user_data['id'] = data.split('"id":')[1]
                except IndexError:
                    pass
                try:
                    user_data['node_id'] = data.split('"node_id":')[1]
                except IndexError:
                    pass
                try:
                    user_data['avatar'] = data.split('"avatar_url":')[1]
                except IndexError:
                    pass
                try:
                    user_data['api'] = data.split('"url":')[1]
                except IndexError:
                    pass
                try:
                    user_data['followers'] = data.split('"followers_url":')[1]
                except IndexError:
                    pass
                try:
                    user_data['following'] = data.split('"following_url":')[1]
                except IndexError:
                    pass
                try:
                    user_data['repos'] = data.split('"repos_url":')[1]
                except IndexError:
                    pass
        if self.verbose:
            for item in user_data.keys():
                print item + ": " + user_data[item]
        return user_data

    def pull_user_repository_list(self):
        repo_list = urllib.urlopen(self.user_data['repos'].replace('"','')).read()
        repo_data = {}
        user_repo_break = self.user_name+'","id":'+self.user_data['id']+',"node_id'

        n_repos = len(repo_list.split(user_repo_break))-1
        if self.verbose:
            print '\033[1m\033[32m' + self.user_name + '\033[0m has \033[1m\033[36m' + str(n_repos) + \
                  '\033[0m github repositories'
        ii = 0
        for entry in repo_list.split(user_repo_break):
            repo_data[ii] = entry
            ii += 1
        return repo_list, n_repos

    @staticmethod
    def git_push():
        os.system('git status')
        os.system('git commit -m "Automated Commit"')
        os.system('git push origin')

    def get_repo_root(self, repo):
        repo = repo + '/master/root.txt'
        uri = 'https://raw.githubusercontent.com/' + self.user_name + '/' + repo
        return urllib.urlopen(uri).read()

    @staticmethod
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

    def get_user_followers(self):
        follow_data = urllib.urlopen(self.user_data['followers'].replace('"','')).read()
        followers = {}
        for entry in follow_data.split('login'):
            follow = []
            try:
                follower = entry.split(',')[0]
                if follower != '[{"':
                    follow.append(follower.replace('"',''))
                    followers[follower] = follow
            except IndexError:
                pass
            try:
                id = entry.split(',')[1].replace('"','')
                follow.append(id)
            except IndexError:
                pass
            try:
                node_id = entry.split(',')[2].replace('"','')
                follow.append(node_id)
            except IndexError:
                pass
            try:
                avatar = entry.split(',')[3].replace('"','')
                follow.append(avatar)
            except IndexError:
                pass
            try:
                followers[follower] = follow
            except KeyError:
                pass
        print self.user_name + ' has ' + str(len(followers.keys())-1) + ' Followers'
        print followers.values()[0]
        return followers


def main():
    if 'p' in sys.argv:
        GIT.git_push()

    if '-u' in sys.argv:
        g = GIT(sys.argv[2], False)

    else:
        user_name = str(input('Enter Github Username:'))
        g = GIT(user=user_name,verbosity=True)


if __name__ == '__main__':
    main()
