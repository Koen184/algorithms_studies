import hashlib


def hash_password(input_password):
    choose_move = 2
    first_number = 7
    salt = 14

    hash_code = bin(salt)[2:]

    for letter in input_password:
        letter_bit = bin(ord(letter))[2:]
        hash_code += letter_bit
        hash_code = bin((int(hash_code, 2) * first_number) >> choose_move)[2:]
        hash_code = bin(int(hash_code, 2) % (2 ** 31 - 1))[2:]

    password_code = ''

    for value in range(0, len(hash_code), 7):
        bits = hash_code[value:value + 7]
        number = int(bits, 2)
        password_code += str(number)

    print(hash_code)
    print(password_code)

    return password_code


def hashlib_password(input_password):
    salt = b'9'

    password_salt = input_password.encode('utf-8') + salt

    sha256_hash = hashlib.sha256()
    sha256_hash.update(password_salt)
    hashed = sha256_hash.hexdigest()

    return hashed


def check_password(password_to_check, password_hashed):
    code = hash_password(password_to_check)
    code_2 = password_hashed

    if code == code_2:
        print('Passwords are the same!')
    else:
        print('Passwords are different :c')


# TESTING
password = input('Input password: ')
hashed_password = hash_password(password)

password_2 = input('Input password to check: ')
check_password(password_2, hashed_password)

hashed_password = hashlib_password(password)
print("Hashed password:", hashed_password)
