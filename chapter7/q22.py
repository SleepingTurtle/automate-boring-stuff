import re

regex22 = re.compile(r'''(
        (Alice|Bob|Carol)
        (\s)
        (eats|pets|throws)
        (\s)
        (apples|cats|baseballs)
)''', re.I)

print("1: " + regex22.search('Alice eats apples.').group())
print("2: " + regex22.search('Bob pets cats.').group())
print("3: " + regex22.search('Carol throws baseballs.').group())
