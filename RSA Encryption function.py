import math

def simple_rsa_demo(p: int, q: int, message: int):
    """
    Demonstrate RSA encryption with small primes.

    WARNING: This is for learning only - real RSA uses huge primes!

    Args:
        p, q: Two prime numbers
        message: Integer to encrypt (must be < p*q)

    Returns:
        Dictionary with keys, encrypted message, and decrypted message

    Steps:
    1. Calculate n = p * q
    2. Calculate φ(n) = (p-1)(q-1)
    3. Choose e (commonly 65537 if it works)
    4. Calculate d (modular inverse of e mod φ(n))
    5. Encrypt: c = m^e mod n
    6. Decrypt: m = c^d mod n
    """
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    if e >= phi_n:
        e = 17

    while math.gcd(e, phi_n) != 1:
        e += 2

    d = pow(e, -1, phi_n)
    encrypted = pow(message, e, n)
    decrypted = pow(encrypted, d, n)

    print("=" * 50)
    print("RSA ENCRYPTION DEMONSTRATION")
    print("=" * 50)
    print(f"\n🔢 Prime Numbers: p = {p}, q = {q}")
    print(f"📐 Modulus (n): {n}")
    print(f"📐 Euler's Totient φ(n): {phi_n}")
    print(f"\n🔓 Public Key:  (n={n}, e={e})")
    print(f"🔐 Private Key: (n={n}, d={d})")
    print(f"\n📨 Original Message:  {message}")
    print(f"🔒 Encrypted Message: {encrypted}")
    print(f"🔓 Decrypted Message: {decrypted}")
    print(f"\n✅ Success! Message decrypted correctly: {message == decrypted}")
    print("=" * 50)

    return {
        'n': n,
        'public_key': (n, e),
        'private_key': (n, d),
        'phi_n': phi_n,  # Optional, just for learning
        'original_message': message,
        'encrypted': encrypted,
        'decrypted': decrypted
    }


print("\n--- Testing RSA encryption ---")
result1 = simple_rsa_demo(61, 53, 123)
print(result1)
print("\n--- Additional RSA tests ---")
test_cases = [
    (17, 11, 42),
    (23, 19, 100),
    (29, 31, 500)
    ]
for p, q, msg in test_cases:
    result = simple_rsa_demo(p, q, msg)
    print(result)