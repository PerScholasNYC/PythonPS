from sys import argv
# read the WYSS section for how to run this
script, Stories, Action = argv

print("The script is called:", script)
print("User loves:",Stories)
print("User loves:",Action )

Heroic_Title = input("Cool title that people will know you by?>")
home = input ("Where are you from?>")
weapon = input("Weapon of choice?>")
Battle_Cry = input("Famous line you say before battle?>")

print(f"""This is the legendary tale of a warrior who hails from the kingdom of {home}.\
This warrior has only been seen by a few, but known by everyone for stopping the alien\
invasion of {home}. Some know this warrior for gracing the battle field with an angelic\
presence while weilding a {weapon}. Others know this hero because of its famous saying {Battle_Cry}.\
No one will ever forget the bravery of the great {Heroic_Title} of {home}
""")
