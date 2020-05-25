from string import ascii_lowercase as abc
from re import sub

# s = [x for x in plain_text.lower() if x.isalpha() or x.isdigit()]
# out = [abc[25 - abc.index(x)] if x.isalpha() else x for x in s]
# cipher = abc[::-1]
# return plain_text.translate(str.maketrans(cipher, abc))

# s = sub(r'[\W]', '', plain_text.lower())
# out = s.translate(str.maketrans(abc, abc[::-1]))


def encode(plain_text):
    s = sub(r'[\W]', '', plain_text.lower()).translate(str.maketrans(abc, abc[::-1]))
    return ' '.join(''.join(s[i:i+5]) for i in range(0, len(s), 5))


def decode(ciphered_text):
    return ''.join(encode(ciphered_text).split())


q = encode("yes"), "bvh"
q
q = encode("no"), "ml"
q
q = encode("OMG"), "lnt"
q
q = encode("O M G"), "lnt"
q
q = encode("mindblowingly"), "nrmwy oldrm tob"
q
q = encode("Testing,1 2 3, testing."), "gvhgr mt123 gvhgr mt"
q
q = encode("Truth is fiction."), "gifgs rhurx grlm"
q
