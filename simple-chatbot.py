import re

# r = "(hi|hello|hey)[ ]*([a-z]*)"
r = r"[^a-z]*([y]o|[h']?ello|ok|hey|(good[ ])?(morn[gin']{0,3}|afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})"
# result = re.match(r, "Hello mario, tudo bem?", flags=re.IGNORECASE)
# result = re.match(r, "hi ho, hi ho, it's off to work...", flags=re.IGNORECASE)
re_greeting = re.compile(r, flags=re.IGNORECASE)

print(re_greeting.match("Hello Rosa").groups())
print(re_greeting.match("Good morning rosa"))
print(re_greeting.match("Yo brow"))
