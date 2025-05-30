import base64
import sys
import urllib.parse

def print_banner():
    print("\n" + "="*40)
    print("🔒 DECO.PY — MULTI-DECODER & ENCODER TOOL")
    print("="*40 + "\n")
    print("Made by @yxn_a on github.com, Monero Donations: \n843FpDw81j3VSVUeoKRbuaGEVuYRkUxum7A3PHXtBPHoK7uZEUKcu39jnNEAVfiKQe82RTiU2DUgRQpGjJWAyrKbKJpUdML\n")

def ask_continue():
    choice = input("\n🔒 Press ENTER to continue decoding or 'q' to quit: ").strip().lower()
    if choice == 'q':
        print("\n❤ Exiting deco.py. Bye!")
        sys.exit()

def base64_menu():
    while True:
        print("\nBASE64 OPTIONS:")
        print("  (1) Decode")
        print("  (2) Encode")
        print("  (q) Quit to main menu")
        choice = input("Select an option: ").strip().lower()
        if choice == '1':
            decode_base64()
        elif choice == '2':
            encode_base64()
        elif choice == 'q':
            return
        else:
            print("❌ Invalid option. Please try again.")

def decode_base64():
    print("✔ BASE64 INPUT TO DECODE: ", end='')
    data = input()
    try:
        decoded = base64.b64decode(data).decode("utf-8")
        print("\n✔ DECODED TEXT:\n" + decoded)
    except Exception as e:
        print("❌ Error decoding Base64:", e)

def encode_base64():
    print("✔ TEXT INPUT TO ENCODE BASE64: ", end='')
    data = input()
    try:
        encoded = base64.b64encode(data.encode("utf-8")).decode("utf-8")
        print("\n✔ ENCODED BASE64:\n" + encoded)
    except Exception as e:
        print("❌ Error encoding Base64:", e)

def base32_menu():
    while True:
        print("\nBASE32 OPTIONS:")
        print("  (1) Decode")
        print("  (2) Encode")
        print("  (q) Quit to main menu")
        choice = input("Select an option: ").strip().lower()
        if choice == '1':
            decode_base32()
        elif choice == '2':
            encode_base32()
        elif choice == 'q':
            return
        else:
            print("❌ Invalid option. Please try again.")

def decode_base32():
    print("✔ BASE32 INPUT TO DECODE: ", end='')
    data = input()
    try:
        decoded = base64.b32decode(data).decode("utf-8")
        print("\n✔ DECODED TEXT:\n" + decoded)
    except Exception as e:
        print("❌ Error decoding Base32:", e)

def encode_base32():
    print("✔ TEXT INPUT TO ENCODE BASE32: ", end='')
    data = input()
    try:
        encoded = base64.b32encode(data.encode("utf-8")).decode("utf-8")
        print("\n✔ ENCODED BASE32:\n" + encoded)
    except Exception as e:
        print("❌ Error encoding Base32:", e)

def hex_menu():
    while True:
        print("\nHEX OPTIONS:")
        print("  (1) Decode")
        print("  (2) Encode")
        print("  (q) Quit to main menu")
        choice = input("Select an option: ").strip().lower()
        if choice == '1':
            decode_hex()
        elif choice == '2':
            encode_hex()
        elif choice == 'q':
            return
        else:
            print("❌ Invalid option. Please try again.")

def decode_hex():
    print("✔ HEX INPUT TO DECODE: ", end='')
    data = input()
    try:
        decoded = bytes.fromhex(data).decode("utf-8")
        print("\n✔ DECODED TEXT:\n" + decoded)
    except Exception as e:
        print("❌ Error decoding HEX:", e)

def encode_hex():
    print("✔ TEXT INPUT TO ENCODE HEX: ", end='')
    data = input()
    try:
        encoded = data.encode("utf-8").hex()
        print("\n✔ ENCODED HEX:\n" + encoded)
    except Exception as e:
        print("❌ Error encoding HEX:", e)

def binary_menu():
    while True:
        print("\nBINARY OPTIONS:")
        print("  (1) Decode")
        print("  (2) Encode")
        print("  (q) Quit to main menu")
        choice = input("Select an option: ").strip().lower()
        if choice == '1':
            decode_binary()
        elif choice == '2':
            encode_binary()
        elif choice == 'q':
            return
        else:
            print("❌ Invalid option. Please try again.")

def decode_binary():
    print("✔ BINARY INPUT TO DECODE (space-separated bits): ", end='')
    data = input()
    try:
        decoded = ''.join([chr(int(b, 2)) for b in data.strip().split()])
        print("\n✔ DECODED TEXT:\n" + decoded)
    except Exception as e:
        print("❌ Error decoding Binary:", e)

def encode_binary():
    print("✔ TEXT INPUT TO ENCODE BINARY: ", end='')
    data = input()
    try:
        encoded = ' '.join(format(ord(c), '08b') for c in data)
        print("\n✔ ENCODED BINARY:\n" + encoded)
    except Exception as e:
        print("❌ Error encoding Binary:", e)

def rot13_menu():
    while True:
        print("\nROT13 OPTIONS:")
        print("  (1) Decode")
        print("  (2) Encode")
        print("  (q) Quit to main menu")
        choice = input("Select an option: ").strip().lower()
        if choice == '1':
            decode_rot13()
        elif choice == '2':
            encode_rot13()
        elif choice == 'q':
            return
        else:
            print("❌ Invalid option. Please try again.")

def rot13_decrypt(text):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - base + 13) % 26
            result.append(chr(base + offset))
        else:
            result.append(char)
    return ''.join(result)

def decode_rot13():
    print("✔ ROT13 INPUT TO DECODE: ", end='')
    data = input()
    print("\n✔ DECODED TEXT:\n" + rot13_decrypt(data))

def encode_rot13():
    print("✔ TEXT INPUT TO ENCODE ROT13: ", end='')
    data = input()
    print("\n✔ ENCODED TEXT:\n" + rot13_decrypt(data))

def url_menu():
    while True:
        print("\nURL ENCODE OPTIONS:")
        print("  (1) Decode")
        print("  (2) Encode")
        print("  (q) Quit to main menu")
        choice = input("Select an option: ").strip().lower()
        if choice == '1':
            decode_url()
        elif choice == '2':
            encode_url()
        elif choice == 'q':
            return
        else:
            print("❌ Invalid option. Please try again.")

def decode_url():
    print("✔ URL-ENCODED INPUT TO DECODE: ", end='')
    data = input()
    print("\n✔ DECODED TEXT:\n" + urllib.parse.unquote(data))

def encode_url():
    print("✔ TEXT INPUT TO ENCODE URL: ", end='')
    data = input()
    print("\n✔ ENCODED URL:\n" + urllib.parse.quote(data))

def caesar_menu():
    while True:
        print("\nCAESAR CIPHER OPTIONS (default shift=13):")
        print("  (1) Decode")
        print("  (2) Encode")
        print("  (q) Quit to main menu")
        choice = input("Select an option: ").strip().lower()
        if choice == '1':
            caesar_decrypt_menu()
        elif choice == '2':
            caesar_encrypt_menu()
        elif choice == 'q':
            return
        else:
            print("❌ Invalid option. Please try again.")

def get_caesar_shift(default_shift=13):
    shift_input = input(f"✔ Enter shift (leave empty for default {default_shift}): ").strip()
    if shift_input == '':
        return default_shift
    try:
        return int(shift_input) % 26
    except ValueError:
        print("❌ Invalid shift, using default:", default_shift)
        return default_shift

def caesar_encrypt(text, shift):
    return ''.join(chr((ord(c) - base + shift) % 26 + base) if c.isalpha()
                   else c for c in text for base in [ord('A') if c.isupper() else ord('a')])

def caesar_decrypt(text, shift):
    return ''.join(chr((ord(c) - base - shift) % 26 + base) if c.isalpha()
                   else c for c in text for base in [ord('A') if c.isupper() else ord('a')])

def caesar_encrypt_menu():
    print("✔ TEXT INPUT TO ENCODE CAESAR: ", end='')
    data = input()
    shift = get_caesar_shift()
    print(f"\n✔ ENCODED TEXT with shift={shift}:\n" + caesar_encrypt(data, shift))

def caesar_decrypt_menu():
    print("✔ CAESAR CIPHER INPUT TO DECODE: ", end='')
    data = input()
    shift = get_caesar_shift()
    print(f"\n✔ DECODED TEXT with shift={shift}:\n" + caesar_decrypt(data, shift))

def atbash_menu():
    while True:
        print("\nATBASH CIPHER OPTIONS:")
        print("  (1) Decode")
        print("  (2) Encode")
        print("  (q) Quit to main menu")
        choice = input("Select an option: ").strip().lower()
        if choice in ['1', '2']:
            print("✔ ATBASH INPUT: ", end='')
            data = input()
            print("\n✔ RESULT:\n" + atbash_decrypt(data))
        elif choice == 'q':
            return
        else:
            print("❌ Invalid option. Please try again.")

def atbash_decrypt(text):
    return ''.join(
        chr(ord('Z') - (ord(c) - ord('A'))) if c.isupper() else
        chr(ord('z') - (ord(c) - ord('a'))) if c.islower() else c
        for c in text
    )

MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9',
    '/': ' '
}
MORSE_CODE_REVERSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def morse_menu():
    while True:
        print("\nMORSE CODE OPTIONS:")
        print("  (1) Decode")
        print("  (2) Encode")
        print("  (q) Quit to main menu")
        choice = input("Select an option: ").strip().lower()
        if choice == '1':
            decode_morse()
        elif choice == '2':
            encode_morse()
        elif choice == 'q':
            return
        else:
            print("❌ Invalid option. Please try again.")

def decode_morse():
    print("✔ MORSE INPUT (use / for space between words): ", end='')
    data = input()
    words = data.strip().split(' / ')
    decoded = ' '.join(''.join(MORSE_CODE_DICT.get(letter, '?') for letter in word.split()) for word in words)
    print("\n✔ DECODED TEXT:\n" + decoded)

def encode_morse():
    print("✔ TEXT INPUT TO ENCODE: ", end='')
    data = input().upper()
    encoded = ' / '.join(' '.join(MORSE_CODE_REVERSE_DICT.get(c, '?') for c in word) for word in data.split())
    print("\n✔ ENCODED MORSE:\n" + encoded)

def ascii_decimal_menu():
    while True:
        print("\nASCII DECIMAL OPTIONS:")
        print("  (1) Decode")
        print("  (2) Encode")
        print("  (q) Quit to main menu")
        choice = input("Select an option: ").strip().lower()
        if choice == '1':
            decode_ascii_decimal()
        elif choice == '2':
            encode_ascii_decimal()
        elif choice == 'q':
            return
        else:
            print("❌ Invalid option. Please try again.")

def decode_ascii_decimal():
    print("✔ ASCII DECIMAL INPUT (space-separated): ", end='')
    data = input()
    decoded = ''.join(chr(int(num)) for num in data.split())
    print("\n✔ DECODED TEXT:\n" + decoded)

def encode_ascii_decimal():
    print("✔ TEXT INPUT TO ENCODE: ", end='')
    data = input()
    encoded = ' '.join(str(ord(c)) for c in data)
    print("\n✔ ENCODED ASCII:\n" + encoded)

def vigenere_menu():
    while True:
        print("\nVIGENÈRE CIPHER OPTIONS:")
        print("  (1) Decode")
        print("  (2) Encode")
        print("  (q) Quit to main menu")
        choice = input("Select an option: ").strip().lower()
        if choice == '1':
            decode_vigenere()
        elif choice == '2':
            encode_vigenere()
        elif choice == 'q':
            return
        else:
            print("❌ Invalid option. Please try again.")

def vigenere_encrypt(text, key):
    key = key.lower()
    return ''.join(
        chr((ord(c) - base + ord(key[i % len(key)]) - ord('a')) % 26 + base) if c.isalpha() else c
        for i, c in enumerate(text)
        for base in [ord('A') if c.isupper() else ord('a')]
    )

def vigenere_decrypt(text, key):
    key = key.lower()
    return ''.join(
        chr((ord(c) - base - (ord(key[i % len(key)]) - ord('a'))) % 26 + base) if c.isalpha() else c
        for i, c in enumerate(text)
        for base in [ord('A') if c.isupper() else ord('a')]
    )

def encode_vigenere():
    print("✔ TEXT INPUT TO ENCODE: ", end='')
    text = input()
    print("✔ KEY: ", end='')
    key = input()
    print("\n✔ ENCODED TEXT:\n" + vigenere_encrypt(text, key))

def decode_vigenere():
    print("✔ TEXT INPUT TO DECODE: ", end='')
    text = input()
    print("✔ KEY: ", end='')
    key = input()
    print("\n✔ DECODED TEXT:\n" + vigenere_decrypt(text, key))

def main_menu():
    while True:
        print_banner()
        print("Select a decoding/encoding method:")
        print("  (1) Base64")
        print("  (2) Base32")
        print("  (3) Hex")
        print("  (4) Binary")
        print("  (5) ROT13")
        print("  (6) URL Encode")
        print("  (7) Caesar Cipher")
        print("  (8) Atbash Cipher")
        print("  (9) Morse Code")
        print(" (10) ASCII Decimal")
        print(" (11) Vigenère Cipher")
        print("  (q) Quit")
        choice = input("Select option: ").strip().lower()

        if choice == '1':
            base64_menu()
        elif choice == '2':
            base32_menu()
        elif choice == '3':
            hex_menu()
        elif choice == '4':
            binary_menu()
        elif choice == '5':
            rot13_menu()
        elif choice == '6':
            url_menu()
        elif choice == '7':
            caesar_menu()
        elif choice == '8':
            atbash_menu()
        elif choice == '9':
            morse_menu()
        elif choice == '10':
            ascii_decimal_menu()
        elif choice == '11':
            vigenere_menu()
        elif choice == 'q':
            print("\n❤ Thanks for using deco.py. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
