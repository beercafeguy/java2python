import string

print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.octdigits)
print(string.whitespace)

flag = 'ABD' in string.ascii_letters  # false
print(flag)
flag='4' in '13579'
print(flag)

flag='a' in 'aeiou'
print(flag)


def is_vowel(ch):
    return ch.lower() in 'aeiou'


print(is_vowel('A'))
print(is_vowel('B'))

"""all upper chars """
print(string.ascii_uppercase)
for ch in string.ascii_uppercase:
    print(ch)

for ch in string.ascii_lowercase:
    print(ch)

for ch in string.digits:
    print(ch)

for ch in string.ascii_lowercase:
    if not is_vowel(ch):
        print(ch)

string_ex="This \n \nis\n great string"
for part in string_ex.splitlines():
    print(part)


print("Hem"+" Chandra")
print("2"*20)

if "Hem" == "Hem":
    print("true")
