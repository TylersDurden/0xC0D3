import urllib
import sys, os


def create_basic_html_doc(title, page_name):
    top = '<!doctype html>\n<body>\n    <head>\n        <title>'+title+\
          '</title>\n        <meta charset=utf-8>\n    </head>\n</body>\n</html>'
    print top
    open(page_name, 'a').write(top)


def create_tunnel_filesystem(name, path):
    top = '<!doctype html>\n<body>\n    <head>\n        <title>' + name + \
          '</title>\n        <meta charset=utf-8>\n    </head>\n'' \
          ''<a href="file:///"'+path+'>' + path+'</a>\n</body>\n</html>'

    print top
    open(name, 'a').write(top)


def main():
    if '-pi_drop' in sys.argv:
        # create_basic_html_doc('[AWX]: (A)utomated (W)eb e(X)tension', 'templates/awx.html')
        create_tunnel_filesystem('R4S83RRY', '/home/pi/Dropper')


if __name__ == '__main__':
    main()
