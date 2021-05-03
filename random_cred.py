import random

mail = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
names = ["suresh", "radhe", "tej", "tanya", "shubham", "rupal", "tushar", "vinay", "shlok"]
ran_name = random.choice(names)
user="user"+ran_name


lower = 10**(10-1)
upper = 10**10 - 1
mob = random.randint(lower, upper)

ran = []
for a in range(4):
    ran.extend(random.choice(mail))
man="a"
for a in ran:
    man=man+a

ranemail = (man+"@gmail.com")