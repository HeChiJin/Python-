guests = ['Raidian','Blaze','Mantra','Misery','FrostNova']
for i in range(len(guests)):
    print(f"{guests[i]}, welcome to my party!")

cannont_come = 'FrostNova'
guests.remove(cannont_come)
print(guests)
print(f"{cannont_come} is dead.")

guests.append('Menchanist')
for i in range(len(guests)):
    print(f"{guests[i]}, welcome to my party!")

guests.insert(0,'Amiya')
guests.insert(2,'Mon3tr')
guests.append('Wishdale')
for i in range(len(guests)):
    print(f"{guests[i]}, welcome to my party!")
print(f"I've invited {len(guests)} members.")

while(len(guests)>2):
    sorry_notice = guests.pop(len(guests)-1)
    print(f"{sorry_notice}, I'm sorry to tell you that you cannot come to my party this time.")
print(f"{guests[0]}, you can still attend my party.")
print(f"{guests[1]}, you can still attend my party.")

del guests[1]
del guests[0]
print(guests)