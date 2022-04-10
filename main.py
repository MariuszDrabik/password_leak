from requests import get
import hashlib


class LengthException(Exception):
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


class SpecialCharException(Exception):
    pass


class LetterException(Exception):
    pass


class NumberException(Exception):
    pass


class PwnedException(Exception):
    pass


class IsLeaked:

    API = 'https://api.pwnedpasswords.com/range/'

    def __init__(self, passwd):
        self.passwd = passwd
        self._hashed = None
        self._leaked = []
        self._hashing()

    def _hashing(self):
        hashed = hashlib.sha1(self.passwd.encode())
        self._hashed = hashed.hexdigest()

    def get_hashes_from_api(self):
        passwd = IsLeaked.API + self._hashed[:5]
        request = get(passwd)
        self._leaked = [i.split(':')[0].strip() for i in request.text.split()]
        
    def pawned_passwd(self):
        self.get_hashes_from_api()
        if self._hashed.upper()[5:] in self._leaked:
            raise PwnedException('Password leaked')
        return True


class PasswordValidator:
    def __init__(self, passwd):
        self.passwd = passwd
        self.validate = False

    def length_check(self):
        if len(self.passwd) < 8:
            raise LengthException('Password is too short budy')
        return True

    def caps_check(self):
        for char in self.passwd:
            if char.isupper():
                return True
        raise LetterException('Password has not any capital letter')

    def lower_check(self):
        for char in self.passwd:
            if char.islower():
                return True
        raise LetterException('Password has not any lower letter')

    def numbers_check(self):
        for char in self.passwd:
            if char.isnumeric():
                return True
        raise NumberException('Password has not any number')

    def special_char_check(self):
        special_characters = '"!@#$%^&*()-+?_=,<>/|\\[]{}'
        if any(char in special_characters for char in self.passwd):
            return True
        raise SpecialCharException('Password has not any special character')

    def check(self):
        checks = (self.length_check(),
                  self.caps_check(),
                  self.lower_check(),
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
                    if PasswordValidator(passwd).check():
                        if IsLeaked(passwd).pawned_passwd():
                            with open('good_passwd.txt', mode='a', encoding='utf8') as good:
                                good.write(f'{passwd}\n')
                except (LengthException,
                        SpecialCharException,
                        LetterException,
                        NumberException,
                        PwnedException) as e:
                    with open('weak_passwd.txt', mode='a', encoding='utf8') as bad:
                        bad.write(f'{passwd}: {e}\n')


if __name__ == '__main__':
    Main().run()
