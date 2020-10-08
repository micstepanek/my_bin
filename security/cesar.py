#!/usr/bin/env python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
    def encrypt_letter(letter):
        position = alphabet.index(letter)
        destination = position - k
        if destination < 0:
            destination + 26
        return alphabet[destination]
    return [encrypt_letter(x) for x in plaintext]

print(encrypt('abcd', 1))