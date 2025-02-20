def scanner_checker(character):
    if type(character) is str:
        return 'string'
    elif type(character) is int:
        return 'integer'
    elif type(character) is float:
        return 'float'
    elif type(character) is bool:
        return 'boolean'


while True:
    character = input('Enter a character: ')
    if character == '*':
        break
    print(f'{character} is a {scanner_checker(character)}')
