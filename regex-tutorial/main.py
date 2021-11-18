import re

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

luba.com

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Scha25fer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

"""

emails = """
    CoreyMSchafer@gmail.com
    corey.schafer@university.edu
    corey-321-schafer@my-work.net
    """

sentence = "Start a sentence and then bring it to an end"

urls = """
https://www.google.asdfasdfas.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

# normal text
# pattern = re.compile(r"[89]0{2}[-.]\d{3}[-.]\d{4}")
# pattern = re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*")
# pattern = re.compile(r"[^b]at")

# emails
# pattern = re.compile(r"[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)")
# pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

# numbers of phones
# with open("regex-tutorial/data.txt", "r") as f:
#     content = f.read()
#     matches = pattern.finditer(content)

# urls
# pattern = re.compile(
#     r"https?://(www\.)?(\w+\.)+(\w+)"
# )  # good idea to separete in groups with parenthesis

pattern = re.compile(r"")

matches = pattern.finditer(urls)  # findall, match


# replacing
# replaced_urls = pattern.sub(r"\2\3", urls)


# the match object have a method to extract the groups
# based on what you passed as a pattern
for match in matches:
    print(match)
    print(match.group(0))
    print(match.group(2), "\n")


# reference: https://www.youtube.com/watch?v=K8L6KVGG-7o
