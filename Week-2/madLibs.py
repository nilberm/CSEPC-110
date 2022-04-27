print("Please enter the following: \n")

adjective = str(input("adjective: ")).lower()
animal = str(input("animal: ")).lower()
verb = str(input("verb: ")).lower()
exclamation = str(input("exclamation: "))
verb2 = str(input("verb: ")).lower()
verb3 = str(input("verb: ")).lower()
animal2 = str(input("animal: ")).lower()
article = ''
if animal2[0] in 'aeiou':
    article = "an"
else:
    article = "a"

print("Your story is: \n")

print(f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb} down the hallway. "{exclamation}!" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family. The funny thing was when {article} {animal2} showed up and started to play with the {animal}. My family will never forget that.')

