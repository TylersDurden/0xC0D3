import hashlib, os, sys, utility
from Crypto.Cipher import AES


def encrypt_file(fname, destructive):
    d_key = hashlib.sha256(str(input('\nEnter Encryption/Decryption Key:'))).digest()
    data = utility.swap(fname, destructive)
    clear_text = ''
    ln = 0
    for line in data:
        clear_text += line + '\n'
        ln += 1
    padding = len(list(clear_text)) % 16

    for space in range(16 - padding):
        clear_text += '0'
    padding = len(list(clear_text)) % 16

    for space in range(padding):
        clear_text += '0'
    return AES.AESCipher(d_key).encrypt(clear_text), d_key


def decrypt_file(file_in, key_file, destroy):
    os.system('cat ' + key_file + " >> key_data.txt")
    key = utility.list2str(utility.swap('key_data.txt', destroy))
    cipher_text = utility.list2str(utility.swap(file_in, destroy))
    padding = len(list(cipher_text)) % 16
    for space in range(16 - padding):
        cipher_text += '0'
    # TODO: Losing end of file during decryption!
    decrypted_data = AES.AESCipher(key).decrypt(cipher_text)
    open('decrypted.txt','w').write(decrypted_data)


def main():
    # File Encryption
    if '-e' in sys.argv:
        file_in = sys.argv[2]
        data, priv_key = encrypt_file(file_in, False)
        file_out = sys.argv[3]
        open(file_out, 'w').write(data)
        open('key', 'w').write(priv_key)
        # Destroy file in
        if '-destroy' in sys.argv:
            os.remove(file_in)

    # File Decryption
    if '-d' in sys.argv:
        file_in = sys.argv[2]
        key_file = sys.argv[3]
        print decrypt_file(file_in, key_file, False)
        if '-destroy' in sys.argv:
            os.remove(key_file)
            os.remove(file_in)


if __name__ == '__main__':
    main()