import re
def capital_words_spaces(text):
  return re.sub("(\w)([A-Z])", r"\1 \2", text)

text=input()
print(capital_words_spaces(text))
