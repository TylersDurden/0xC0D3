import os, logging, time, datetime
from flask import Flask, render_template, Markup, request


def generate_logfile():
    date = datetime.datetime.now()
    d = date.day
    m = date.month
    y = date.year - 2000
    log_file_name = 'LogFile' + str(m) + str(d) + str(y) + '.txt'
    open(log_file_name, 'a').write('LOGFILE CREATED ' + str(date) + '\n')
    return date, d, m, y, log_file_name


T0 = time.time()
date, d, m, y, log_file_name = generate_logfile()
app = Flask(__name__)
app.config.from_pyfile('settings.py')
cache = {}
logger = logging.getLogger(__name__)


def log_visitor():
    print '\033[1m\033[33m [' + str(time.time() - T0) + 's Elapsed]\033[0m'
    os.system('Visited @ ' + str(date) + '+' + str(time.time() - T0) + 's >> ' + log_file_name)
    usr_ip = ''
    cmd = 'echo $(GET https://ipinfo.io/$(GET https://api.ipify.org)) >> ip.txt'
    try:
        os.system(cmd)
        usr_ip = open('ip.txt', 'r').readlines().pop()
        os.system("echo '" + usr_ip + "' >> " + log_file_name)
    except:
        pass
    os.system('rm ip.txt')
    if usr_ip != '':
        print "\033[1m\033[35m Page visited by:\n" + usr_ip + '\033[0m'


@app.route('/')
def home_page():
    log_visitor()
    return render_template('index.html')


@app.route('/root')
def automated():
    log_visitor()
    return render_template('awx.html')

    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

app.run(debug=True,host='0.0.0.0', port=port)

