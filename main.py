from requests import get
import hashlib

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


