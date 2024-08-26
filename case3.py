
g = 5
public_key = 1953125
c1 = 15625
c2 = 832667268468867405317723751068115234375

# Step 1: Find x such that g^x = public_key
def find_exponent(base, result):
    exponent = 0
    while base ** exponent < result:
        exponent += 1
        if base ** exponent == result:
            return exponent
    return None

x = find_exponent(g, public_key)   # public key is g^x
y = find_exponent(g, c1)  # c1 = g ^ y


key = g ** (x * y)


m = c2 // key   # elgamal decryption equation

print("message = " + str(m))
