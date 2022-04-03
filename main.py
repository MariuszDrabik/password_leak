from requests import get
import hashlib


class LengthError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'{self.message}'
        else:
            return 'Password to short'


class SpecialCharError(Exception):
    pass


class CapsError(Exception):
    pass


class NumberError(Exception):
    pass


class PwnedException(Exception):
    pass


password_to_hash = "oko123"

passwd_hashed = hashlib.sha1(password_to_hash.encode())
# hashed on site to check if it working:
sample = 'a82bfd23636292f19c7663684be63713dc04dfe2'

print("The hexadecimal equivalent of SHA-1 is : ")
print(passwd_hashed.hexdigest())
print(sample)
api = 'https://api.pwnedpasswords.com/range/'

# request = get(api)
# print(request.status_code)


class IsLeaked:
    def __init__(self, passwd):
        self.passwd = passwd

    def hashing(self):
        self.hashed = hashlib.sha1(self.passwd.encode())


class PasswordValidator:
    def __init__(self, passwd):
        self.passwd = passwd
        self.validate = False

    def length_check(self):
        if len(self.passwd) < 8:
            raise LengthError('Password is too short budy')
        return True

    def caps_check(self):
        for char in self.passwd:
            if char.isupper():
                return True
        raise CapsError('Password has not any capital letter')

    def numbers_check(self):
        for char in self.passwd:
            if char.isnumeric():
                return True
        raise CapsError('Password has not any number')

    def special_char_check(self):
        special_characters = '\"!@#$%^&*()-+?_=,<>/\|[]\{\}'
        if any(char in special_characters for char in self.passwd):
            return True
        raise SpecialCharError('Password has not any special character')

    def check(self):
        checks = (self.length_check(),
                  self.caps_check(),
                  self.numbers_check(),
                  self.special_char_check(),)
        return all(checks)


class Main:
    def __init__(self):
        pass

    def run(self):
        with open('passwords.txt', mode='r', encoding='utf8') as file:
            for i in file:
                passwd = i.strip()
                try:
                    checked_word = PasswordValidator(passwd)
                    if checked_word.check():
                        print('Zajebiste hasło', passwd)
                except (LengthError,
                        SpecialCharError,
                        CapsError,
                        NumberError) as e:
                    print(passwd, e)



if __name__ == '__main__':
    Main().run()


