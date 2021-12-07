import math

p = 170141183460469231731687303715884105727
q = 43143988327398957279342419750374600193
n = p * q
t = (p-1) * (q-1)

e = 2
while (e < t) and (t % e != 1):
    e += 1
    
d = 1
while (e * d % t == 1) or (d == e):
    d += 1


# 암호화 함수
def encrypt(original_score):  
    power_encrypt = math.pow(original_score, e)
    cipher_text = power_encrypt % n
    return int(cipher_text)


# 복호화 함수
def decrypt(cipher_text):
    power_decrypt = math.pow(cipher_text, d)
    output_score = power_decrypt % n
    return int(output_score)
