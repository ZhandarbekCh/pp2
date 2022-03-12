import re 
snake_case=input() 
pattern=r"(.*?)_([a-zA-z])" 
def toCamel(txt): 
    return txt.group(1)+txt.group(2).upper() 
#res=re.sub(pattern,toCamel,snake_case) 
print(re.sub(pattern,toCamel,snake_case))
