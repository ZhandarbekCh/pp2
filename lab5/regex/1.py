import re
def text_match(text):
        patterns = '^ab*$'
        if re.search(patterns,  text):
                return 'Correct!'
        else:
                return('Incorrect!')

text=input()
print(text_match(text))
