def swap_case(s):
    text = ''
    digits = '0123456789'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    specialchar = '!@#$%^&*()-_=+`~\"\',<.>/?'
    whitespace = ' '
    
    for char in s:
        if char in whitespace:
            text += ' '
        elif char in digits:
            text += char
        elif char in specialchar:
            text += char
        elif char in uppercase:
            text += char.lower()
        elif char in lowercase:
            text += char.upper()
        
    return text