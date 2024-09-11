# Special sequences
import re

# Example 1: \w word character
text = "Hello, my name is Michael_Jackson."

pattern1 = r"\w+"
pattern2 = r"\W+"

matches1 = re.findall(pattern1, text)
matches2 = re.findall(pattern2, text)
print(f"'\w' pattern matches: {matches1}")
print(f"'\W' pattern matches: {matches2}")

# Example 2: \s whitespace character
# Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
text = "Hello, my name is \t\nMichael_Jackson."

pattern1 = r"\s"
pattern2 = r"\S"

matches1 = re.findall(pattern1, text)
matches2 = re.findall(pattern2, text)

print(f"\s pattern matches: {matches1}")
print(f"\S pattern matches: {matches2}")

# Example 3: \d digit character
# numbers from 0-9
text = "Ahmet: 555-555-55-55"

pattern1 = r"\d+"
pattern2 = r"\D+"

matches1 = re.findall(pattern1, text)
matches2 = re.findall(pattern2, text)

print(f"\d pattern matches: {matches1}")
print(f"\D pattern matches: {matches2}")


# Metacharacters

# Example 1: . Any character (except newline character)
text = "I have 9 apples, 5 oranges, 7 pears, 3 qw\nasd"

pattern1 = r"\d ..."

matches1 = re.findall(pattern1, text)
print(matches1)

text2 = "The cat sat at the mat."
pattern2 = r".at"
matches2 = re.findall(pattern2, text2)
print(matches2)


# Example 2: * (asterisk) Zero or more occurrences
text = "abbbc abbc abc adc ac a_c axc a.c"
pattern1 = r"ab*c"
matches = re.findall(pattern1, text)
print(matches)

pattern2 = r"a\w*c"
matches2 = re.findall(pattern2, text)
print(matches2)


# ? (question mark) Zero or one occurences
text = "abbbc abbc abc adc ac a_c axc a.c"
pattern1 = r"ab?c"   # abc ac
matches1 = re.findall(pattern1, text)
print(matches1)

pattern2 = r"a\w?c"   #
matches2 = re.findall(pattern2, text)
print(matches2)


# + (plus) One or more occurences
text = "abbbc abbc abc adc ac a_c axc a.c"
pattern1 = r"ab+c"   # abbbc abbc abc
matches1 = re.findall(pattern1, text)
print(matches1)

pattern2 = r"a\w+c"
matches2 = re.findall(pattern2, text)
print(matches2)



# example 5 : | pipe

text = "I have a cat and dog. My cat is cute."
pattern = r"cat|dog"
matches = re.findall(pattern, text)
print(matches)


# exam 6: ^ caret
text = "10 is a number."
pattern = r"^1"
match = re.search(pattern, text)
print(match)

# exam 7  $ ends with
text = "My number is 123-44-61"
pattern = r"\d$"
match = re.search(pattern, text)
print(match)

# exam 8: [] a set of characters
text = "abc ABC def DEF 123 abc_123"
pattern = r"[a-z]"
matches = re.findall(pattern, text)
print(matches)


# exam 9: matching characters exclude
text = "banana orange apple pear strawberry"
pattern = r"[^aei]\w[aeiou]"
matches = re.findall(pattern, text)
print(matches)