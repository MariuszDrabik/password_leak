from modules.PasswdValidator import PasswdValidator
from modules.Exceptions import (
    LengthException,
    LetterException,
    SpecialCharException,
    NumberException,
    PwnedException,
)


class Main:

    def save_good(self, passwd):
        if not passwd:
            passwd = 'All passwords are bad'
        with open('good_passwd.txt', mode='a', encoding='utf8') as file:
            file.write(f'{passwd}\n')

    def save_bad(self, passwd, error):
        with open('weak_passwd.txt', mode='a', encoding='utf8') as file:
            file.write(f'{passwd}: {error}\n')

    def run(self):
        with open('passwords.txt', mode='r', encoding='utf8') as file:
            for i in file:
                passwd = i.strip()
                try:
                    validation = PasswdValidator(passwd)
                    validation.validate()
                    validation.pawned_check()
                    self.save_good(passwd)
                except (LengthException,
                        SpecialCharException,
                        LetterException,
                        NumberException,
                        PwnedException) as e:
                    self.save_bad(passwd, e)


if __name__ == '__main__':
    Main().run()
