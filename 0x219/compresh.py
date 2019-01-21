import urllib, zlib, random, crypt, utility, time, os


def pull_sherlock_ebook():
    url = 'http://gutenberg.pglaf.org/1/6/6/1661/1661.txt'
    sherlock = urllib.urlopen(url).read().decode('utf-8')
    sh_length = len(sherlock)
    return sherlock, sh_length


def zipped(text):
    return zlib.compress(text.encode('ascii'))


def unzip(data):
    return zlib.decompress(data,wbits=None,bufsize=None)


def gen_random_text(sh_len):
    rnd = ''.join([chr(random.randint(0, 126)) for k in range(sh_len)])
    return rnd


def main():
    t0 = time.time()
    sherlock, sh_length = pull_sherlock_ebook()
    pull_time = time.time()-t0
    print "Length of Sherlock Holmes Text is " + str(sh_length) + " characters"
    print "["+str(pull_time)+'s Elapsed]'

    zipped_sherlock = zipped(sherlock)
    zip_time = time.time()
    print "Length of Zipped Sherlock Holmes Text is " + str(len(zipped_sherlock)) + " characters"
    print "Zipped in " + str(time.time()-zip_time)+" seconds"

    write_time = time.time()
    utility.write('sherlock.txt', sherlock)
    print 'Wrote uncompressed Sherlock Holmes text to file sherlock.txt in ' +\
        str(time.time()-write_time) + ' seconds'

    encryption_time = time.time()
    encrypted_sherlock_data, key = crypt.encrypt_file('sherlock.txt', False)
    utility.write('encrypted_sherlock.txt', encrypted_sherlock_data)
    print "Encrypted uncompressed text and wrote to file encrypted_sherlock in " +\
          str(time.time() - encryption_time) + ' seconds'

    decrypt_time = time.time()
    utility.write('key_file', key)
    utility.execute('python crypt.py -d encrypted_sherlock.txt  key_file', False)
    print "Decrypted uncompressed text and wrote to file encrypted_sherlock in " + \
          str(time.time() - decrypt_time) + ' seconds'


if __name__ == '__main__':
    main()

