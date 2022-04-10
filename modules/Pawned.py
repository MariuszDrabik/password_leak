from requests import get
from .Exceptions import PwnedException
import hashlib


class Leaked:

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
        passwd = Leaked.API + self._hashed[:5]
        request = get(passwd)
        self._leaked = [i.split(':')[0].strip() for i in request.text.split()]

    def pawned_passwd(self):
        self.get_hashes_from_api()
        if self._hashed.upper()[5:] in self._leaked:
            raise PwnedException('Password leaked')
        return True
