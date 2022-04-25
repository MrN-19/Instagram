from string import ascii_letters,digits
from random import randint
SYMBOLS = "!@#$%^&*()<>-+\\"
ALL_CHARACTERS = ascii_letters + digits + SYMBOLS
def generate_code(length:int) -> str:
    code = ""
    for i in range(length):
        random_number = randint(0,len(ALL_CHARACTERS) - 1)
        code += ALL_CHARACTERS[random_number]
    return code

def clean_text(text:str) -> str:
    text = text.strip()
    text = text.replace(" ","")
    return text
