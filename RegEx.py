import re

data = 'Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. ' \
       'Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on ' \
       'writing your app without needing to reinvent the wheel. It’s free and open source. pet@gmail.com, lal@mail.ru'

"""
\w+    matches any word character (equal to [a-zA-Z0-9_]
+      Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
@      matches the character @ literally (case sensitive)
.      matches any character (except for line terminators)
\d     matches a digit (equal to [0-9])
\D     matches any character that\'s not a digit (equal to [^0-9])
\w     matches any word character (equal to [a-zA-Z0-9_])
\W     matches any non-word character (equal to [^a-zA-Z0-9_])
\s     matches any whitespace character (equal to [\r\n\t\f\v ])
\S     matches any non-whitespace character (equal to [^\r\n\t\f\v ])
[^abc] Matches any character except for an a, b or c
[^a-z] Matches any characters except those in the range a-z.
(a|b)  Matches the a or the b part of the subexpression.
a?     Matches an `a` character or nothing.
^      Matches the start of a string without consuming any characters. If multiline mode is used, this will also match 
       immediately after a newline character.
$      Matches the end of a string without consuming any characters. If multiline mode is used, this will also match 
       immediately before a newline character.
a*     Matches zero or more consecutive `a` characters.

[0-9]{3}      - looking for 3 digits in a row
\w{6}         - first 6 symbols of every 6+ consisting of words
\w{6}\s       - words that consist of 6 symbols and then is the space
[A-Z][a-z]+   - first letter is capital and then any lowercase number of letters([a-z]+)
@\w+\.\w+     - looking for domain like "@gmail.com"

r'[\w.-]@(?!intel\.com)[A-Za-z-]+\.[\w.]+'    all the domain names without "intel.com"  (?!word) = except "word"
"""

text_looking_for = r'@\w+\.\w+'
all_results = re.findall(text_looking_for, data)
# print(all_results)

# -------------------lesson2-------------------------------------

data_file = open('data.txt', 'r')
emails_file = open('emails.txt', 'w')
my_data = data_file.read()

looking_for = r'[\w.-]+@[\w.-]+'

result = re.findall(looking_for, my_data)
print(len(result))
for res in result:
    emails_file.write(res + '\n')

data_file.close()
emails_file.close()
