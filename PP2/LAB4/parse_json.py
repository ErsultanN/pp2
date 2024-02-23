import json

with open('PP2\LAB4\sample-data.json') as f:
    # print(f)
    data = json.load(f)

# print(data)
    

print("Interface Status")
print("=" * 80)
print("DN" + " " * 48 + "Description" + " " * 9 + "Speed" + " " * 3 + "MTU")
print("-" * 49 + " " + "-" * 11 + " " * 9 + "-" * 5 + " " * 3 + "-" * 3)


for entry in data['imdata']:
    dn = entry['l1PhysIf']['attributes']['dn']
    description = entry['l1PhysIf']['attributes'].get('descr', '')
    speed = entry['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = entry['l1PhysIf']['attributes'].get('mtu', '')
    print(dn.ljust(50) + description.ljust(20) + speed.ljust(8) + mtu.ljust(6))