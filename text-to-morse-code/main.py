def main():
    programme_active = True

    # CONSTANTS
    MINOR_SPACE = "   "
    MAJOR_SPACE = "          "
    TWIN_SPACE = " "

    # MORSE CODE DICTIONARY
    BOOK = {
        '1': '. - - - -',
        '2': '. . - - -',
        '3': '. . . - -',
        '4': '. . . . -',
        '5': '. . . . .',
        '6': '- . . . .',
        '7': '- - . . .',
        '8': '- - - . .',
        '9': '- - - - .',
        '0': '- - - - -',
        '@': '. - - . - .',
        ("A", "a"): ". - ",
        ("B", "b"): "- . . . ",
        ("C", "c"): "- . - .",
        ("D", "d"): "- . .",
        ("E", "e"): ".",
        ("F", "f"): ". . - .",
        ("G", "g"): "- - .",
        ("H", "h"): ". . . .",
        ("I", "i"): ". .",
        ("J", "j"): ". - - -",
        ("K", "k"): "- . -",
        ("L", "l"): ". - . . ",
        ("M", "m"): "- -",
        ("N", "n"): "- .",
        ("O", "o"): "- - -",
        ("P", "p"): ". - - .",
        ("Q", "q"): "- - . -",
        ("R", "r"): ". - .",
        ("S", "s"): ". . .",
        ("T", "t"): "-",
        ("U", "u"): ". . -",
        ("V", "v"): ". . . -",
        ("W", "w"): ". - -",
        ("X", "x"): "- . . -",
        ("Y", "y"): "- . - -",
        ("Z", "z"): "- - . ."
    }

    # FUNCTIONS
    def get_morse(word):
        '''
        Input: String from user
        Compares letters in string to key, value pairs of a dictionary containing the morse encoded_letters conversions
        Output: Morse_code equivalent
        '''

        encoded_letters = []
        previous_letter = None
        for character in word:

            if character == ' ':
                encoded_letters.append(MAJOR_SPACE)
                previous_letter = MAJOR_SPACE
                continue

            for k, v in BOOK.items():
                if character in k:
                    if character == previous_letter:
                        encoded_letters.append(TWIN_SPACE)
                        encoded_letters.append(v)
                        continue
                    if len(encoded_letters) == 0:
                        encoded_letters.append(v)
                        previous_letter = character
                        continue
                    elif previous_letter == MAJOR_SPACE:
                        encoded_letters.append(v)
                        previous_letter = character
                        continue
                    else:
                        encoded_letters.append(MINOR_SPACE)
                        encoded_letters.append(v)
                        previous_letter = character
                        continue
        return encoded_letters

    def output(code):
        '''
        Takes the encoded letters as a list and returns encoded message string
        :param code: The encoded message list
        :return: String of encoded message
        '''
        empty_string = ''
        return empty_string.join(encoded_message)

    def user_input():
        response = str(input('Please provide a String to convert?\n'))
        return response

    def exit_input():
        response = input('Would you like to encode another message?\nType (Y/N)\n').lower()
        return response

    WELCOME_MESSAGE = '''
    +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+
    |M o r s e| |C o d e| |E n c o d e r|
    +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+
    '''

    GOODBYE_MESSAGE = '''
    +-+-+-+-+-+-+-+
    |G o o d| |B y e|
    +-+-+-+-+-+-+-+
    '''

    print(WELCOME_MESSAGE)
    print('Welcome to Morse Code Encoder !! ')

    while programme_active:

        user_response = user_input()
        # Converter functionality
        encoded_message = get_morse(user_response)
        # Output Morse Code
        morse_code_message = output(encoded_message)
        print(morse_code_message)

        # Program Exit
        valid_response = False
        while not valid_response:
            exit_response = exit_input()

            if exit_response == 'n':
                programme_active = False
                valid_response = True
                print('Thank you for using Morse Code Converter')
                print(GOODBYE_MESSAGE)
                break

            elif exit_response == 'y':
                valid_response = True
                break
            else:
                continue


if __name__ == '__main__':
    main()
