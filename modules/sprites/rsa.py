import math
import gmpy2
# from Crypto.Util.number import getPrime


p = 170141183460469231731687303715884105727
q = 43143988327398957279342419750374600193
key = 19
n = p * q


# 암호화 함수
def encrypt(original_score):  
    power = math.pow(original_score, key)
    cipherText = power % n
    return int(cipherText)


# 복호화 함수
def decrypt(ciphertext):
    output_score = gmpy2.iroot(ciphertext, key)[0]
    return int(output_score)