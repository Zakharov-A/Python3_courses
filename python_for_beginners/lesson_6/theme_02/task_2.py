text = input()
letters = 0
digits = 0
spaces = 0
punctuation_marks = 0

for symbol in text:
    if symbol.isalpha():
        letters += 1
    elif symbol.isdigit():
        digits += 1
    elif symbol == ' ':
        spaces += 1
    elif symbol in '.,:!,)':
        punctuation_marks += 1

print(f'The text "{text}" contains {letters} letter(s), 0 number(s), {spaces} space(s) and {punctuation_marks} punctuation mark(s).')

