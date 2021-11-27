import enchant

d = enchant.Dict("en_US")
text = "Scholl"
print(d.check(text))
print(d.suggest(text))
