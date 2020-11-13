# _*_ coding: uft-8 _*_
import hashlib

db = {'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    _md = hashlib.md5()
    if user == bob:
        _md.update(password)
        while(_md.hexdigest() == db[0])
            print("True")