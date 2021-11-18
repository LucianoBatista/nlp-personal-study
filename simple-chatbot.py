import re

r = "(hi|hello|hey)[ ]*([a-z]*)"
# result = re.match(r, "Hello mario, tudo bem?", flags=re.IGNORECASE)
result = re.match(r, "hi ho, hi ho, it's off to work...", flags=re.IGNORECASE)

print(result)
