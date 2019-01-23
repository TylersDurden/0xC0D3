import zlib, os, random, sys


def zipped(text):
    return zlib.compress(text.encode('ascii'))


def unzip(data):
    return zlib.decompress(data,wbits=None,bufsize=None)


def gen_random_text(sh_len):
    rnd = ''.join([chr(random.randint(0, 126)) for k in range(sh_len)])
    return rnd


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def compress_text_file(file_name, zip_file_name, destroy_original):
    raw_data = swap(file_name, destroy_original)
    data = ''
    for line in raw_data:
        data += line + '\n'
    zipped_file_data = zipped(data)
    open(zip_file_name, 'a').write(zipped_file_data)

