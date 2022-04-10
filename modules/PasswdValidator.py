from modules.Pawned import Leaked
from modules.Exceptions import (
    LengthException,
    LetterException,
    SpecialCharException,
    NumberException,
)


class PasswdValidator:
    def __init__(self, passwd):
        self.passwd = passwd

    def length_check(self):
        if len(self.passwd) < 8:
            raise LengthException('Password is too short')
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

    def validate(self):
        checks = (self.length_check(),
                  self.caps_check(),
                  self.lower_check(),
                  self.numbers_check(),
                  self.special_char_check(),)
        return all(checks)

    def pawned_check(self):
        pwned = Leaked(self.passwd)
        return pwned.pawned_passwd()
