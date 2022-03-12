import re 
camelCase=input() 
pattern=r"(.+?)([A-Z])" 
def to_snake(txt): 
    return txt.group(1).lower()+"_"+txt.group(2).lower() 
res=re.sub(pattern,to_snake,camelCase) 
print(res)
