class VigenereCipher:
    # Used to convert letters to 0–25 range
    offset = ord('A')

    def __init__(self, keyword: str):
        # Keyword is stored in uppercase form
        self.keyword = keyword.upper()

    def __shift_letter(self, letter: str, shift: int, forward: bool):
        # Convert character to a number
        base = ord(letter) - self.offset

        # Reverse shift when decrypting
        if not forward:
            shift = -shift

        # Wrap around using modulo
        new_pos = (base + shift) % 26

        # Convert back to letter
        return chr(self.offset + new_pos)

    def __generate_shift_list(self, length: int):
        # Precompute the shift for each position by repeating the keyword
        key = self.keyword
        klen = len(key)
        result = [0] * length

        for idx in range(length):
            result[idx] = ord(key[idx % klen]) - self.offset

        return result

    def encrypt(self, plaintext: str):
        # Keep only A–Z characters
        text = ''.join(ch for ch in plaintext.upper() if ch.isalpha())

        # Compute shift values for each letter
        shifts = self.__generate_shift_list(len(text))

        output = []

        # Apply forward shift
        for pos, ch in enumerate(text):
            output.append(self.__shift_letter(ch, shifts[pos], True))

        return ''.join(output)

    def decrypt(self, ciphertext: str):
        # Remove non-letter characters
        text = ''.join(ch for ch in ciphertext.upper() if ch.isalpha())

        # Generate the same shifts used in encryption
        shifts = self.__generate_shift_list(len(text))

        restored = []

        # Apply backward shift
        for pos, ch in enumerate(text):
            restored.append(self.__shift_letter(ch, shifts[pos], False))

        return ''.join(restored)


def main():
    v = VigenereCipher('smarties')
    c = v.encrypt("The quick brown fox jumps over the lazy dog")
    p = v.decrypt(c)
    assert p == 'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'


if __name__ == "__main__":
    main()

