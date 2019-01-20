import os, hashlib, sys
from Crypto.Cipher import AES


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def write(fname, data):
    for buffer in data:
        open(fname, 'w').write(buffer)


def execute(command, destroy):
    os.system(command+'>> command.txt')
    return swap('command.txt', destroy)


def list2str(words):
    str_out = ''
    for element in words:
        str_out += element
    return str_out


def encrypt_file(fname, destructive):
    d_key = hashlib.sha256(str(input('\nEnter Encryption/Decryption Key:'))).digest()
    data = swap(fname,destructive)
    clear_text = ''
    ln = 0
    for line in data:
        clear_text += line+'\n'
        ln += 1
    padding = len(list(clear_text))%16

    for space in range(16-padding):
        clear_text += '0'
    padding = len(list(clear_text)) % 16

    for space in range(padding):
        clear_text += '0'
    return AES.AESCipher(d_key).encrypt(clear_text), d_key


def decrypt_file(file_in, key_file, destroy):
    """
    Decrypts a given file name, using the key
    provided. The destroy flag indicates
    Whether the encrypted file should be erased.
    :param file_in:
    :param key_file:
    :param destroy:
    :return:
    """
    os.system('cat '+key_file+" >> key_data.txt")
    key = list2str(swap('key_data.txt', destroy))
    cipher_text = list2str(swap(file_in, destroy))
    padding = len(list(cipher_text)) % 16
    for space in range(16 - padding):
        cipher_text += '0'
    # TODO: Losing end of file during decryption!
    return AES.AESCipher(key).decrypt(cipher_text)


def main():
    if '-e' in sys.argv:
        file_in = sys.argv[2]
        data, priv_key = encrypt_file(file_in, False)
        file_out = sys.argv[3]
        open(file_out, 'w').write(data)
        open('key','w').write(priv_key)
    if '-destroy' in sys.argv:
        os.remove(file_in)

    if '-d' in sys.argv:
        file_in = sys.argv[2]
        key_file = sys.argv[3]
        print decrypt_file(file_in, key_file, False)



if __name__ == '__main__':
    main()

