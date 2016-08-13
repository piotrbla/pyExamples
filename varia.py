import unicodedata
import chardet
import re

print(re.sub(r'[\w]', "", "zażółć gęślą jaźń", flags=re.L))
print(re.sub(r'[\w]', "", "zażółć gęślą jaźń"))
# print(re.sub(r'[^a-zóą-ż]', "", "żółćęśąźń"))
# print(re.sub(r'[^A-ZÓĄ-Ż]', "", "ZAŻÓŁĆ GĘŚLĄ JAŹŃ"))
# letters = "ąćńłóśźż"
# chardet.detect(letters.encode("utf-8"))
# print(letters.encode("utf-8"))
# '\xc4\x85\xc4\x87\xc5\x84\xc5\x82\xc3\xb3\xc5\x9b\xc5\xba\xc5\xbc'
# for letter in letters:
#     print(unicodedata.category(letter))
# print(ord("\xc48\x85"))