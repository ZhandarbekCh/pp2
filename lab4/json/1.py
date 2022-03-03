import json

f=open("sample.json")
memory=json.load(f)

print('Interface Status')
print('='*50)
print('DN',' '*15,'Description','Speed', 'MTU', sep=5*' ')
print('-'*50)
y=0
for i in memory['imdata']:
    y+=1
    o1=i["l1PhysIf"]["attributes"]["dn"]
    o2=i["l1PhysIf"]["attributes"]["fecMode"]
    o3=i["l1PhysIf"]["attributes"]["mtu"]

    print(o1,' '*5,o2,' '*2,o3)
    if y==3:
        break
