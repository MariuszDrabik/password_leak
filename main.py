from requests import get
import hashlib

password_to_hash = "Mariusz1"

passwd_hashed = hashlib.sha1(password_to_hash.encode())
sample = 'e01dc0a4ab8236bdaa835dda82dd1d0b401b65bc'

print("The hexadecimal equivalent of SHA-1 is : ")
print(passwd_hashed.hexdigest())
print(sample)
api = 'https://api.pwnedpasswords.com/range/'
# request = get(api)
# print(request.status_code)


