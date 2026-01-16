# ▄
# ▄▄▄

# The ITU International Morse code encodes the 26 basic Latin letters ⟨A⟩ to ⟨Z⟩,
# one accented Latin letter ⟨É⟩, the Indo-Arabic numerals ⟨0⟩ to ⟨9⟩,
# and some punctuation and messaging procedural signals (prosigns)

# The letters of a word are separated by a space of duration equal to three dits,
# and words are separated by a space equal to seven dits

# International Morse code is composed of five elements:[2]: §3 
#
# short mark, dot or dit ( ▄ ): "dit duration" is one time unit long
# long mark, dash or dah ( ▄▄▄ ): three time units long
# inter-element gap between the dits or dahs within a single character:
# one dit duration silence, one unit long
# short gap (between letters): one dah duration silence, three time units long
# medium gap (between words): a long silence, duration the same as two (silent)
# dahs sent with a normal one dit gap, seven time units (formerly five


MORSE_CODE_MAPPINGS_LETTER = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

}

MORSE_CODE_MAPPINGS_NUMBER = {'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
 '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',' ': '/',
# Space between words is represented by a single slash
}

def convert_to_morse_code(text_string):

    morse_code = []
    text_string = text_string.upper()
    for char in text_string:
        if char in MORSE_CODE_MAPPINGS_LETTER:
            morse_code.append(MORSE_CODE_MAPPINGS_LETTER[char])
            morse_code.append(" ")
    return "".join(morse_code).strip()

user_input = input("Enter a string to convert to Morse code: ")
morse_output = convert_to_morse_code(user_input)

print(f"Original string: {user_input}")
print(f"Morse code: {morse_output}")