# Import the 'inverse' function from the 'Cryptodome.Util.number' module
from Cryptodome.Util.number import inverse

# Define the plaintext message 'm' to be encrypted
m = 12

# Define the prime numbers 'p' and 'q' for RSA encryption
p = 3
q = 17

# Calculate the modulus 'n' by multiplying 'p' and 'q'
n = (p * q)

# Calculate Euler's totient function 'phi' for 'n'
phi = (p - 1) * (q - 1)

# Choose the public exponent 'e' (usually a small prime number, commonly 3 or 65537).
e = 5

# Calculate the private exponent 'd' using the modular multiplicative inverse of 'e' modulo 'phi'
d = inverse(e, phi)

# Encrypt the plaintext 'm' using the public key (n, e) and the 'pow' function
c = pow(m, e, n)

# Print the encrypted message.
print(f"The encrypted message is- {c}")

# Decrypt the ciphertext 'c' using the private key (n, d) and the 'pow' function
m = pow(c, d, n)

# Print the decrypted message
print(f"The decrypted message is- {m}")