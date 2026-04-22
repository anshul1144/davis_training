"""11) Encrypt file content using Caesar Cipher and save into a new file."""


def caesar_encrypt(text, shift):
    encrypted = []

    for char in text:
        # Encrypt uppercase letters
        if "A" <= char <= "Z":
            new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            encrypted.append(new_char)
        # Encrypt lowercase letters
        elif "a" <= char <= "z":
            new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            encrypted.append(new_char)
        else:
            # Keep non-letter characters unchanged
            encrypted.append(char)

    return "".join(encrypted)


def encrypt_file(input_file="input.txt", output_file="encrypted.txt", shift=3):
    with open(input_file, "r", encoding="utf-8") as infile:
        content = infile.read()

    encrypted_content = caesar_encrypt(content, shift)

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(encrypted_content)


if __name__ == "__main__":
    encrypt_file()
    print("Encrypted content saved to encrypted.txt")
