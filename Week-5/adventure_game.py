name = input("\nWelcome to my mine RPG game, only white the words that are in CAPSLOOK or the code is going to break!\n\nPlease enter your name: ")

fight_or_run = input("\nYou are a fearless warrior, who finds yourself inside a dungeon, you are there in search of the lost talisman that can bring back the Ghusfor Kingdom back to the hands of the Fortfud royal family, who were taken from their post by the magician Martyst who enchanted the high clergy and all of the elite by deceiving them and making the royal family a fraud. Now you find yourself at the exit of this dungeon and there is a mercenary in front of you who tries to stop you from going back to the Ghusfor Kingdom, you can either try to FIGHT him or RUN and get on your horse that is right after the mercenary waiting for you from the outside the dungeon. [FIGHT/RUN]").lower()

if fight_or_run == 'fight':
    fight_forest_or_mountains = input("\nYou pull out your sword and prepare to fight, the mercenary pulls out his two daggers and rushes to attack you, you stop his blow with your sword and with all your skill and strength throw the mercenary back with your sword and strike him and the blade of his sword cuts the mercenary's chest, who falls dead to the ground. You then take your horse and leave for the city of the Ghusfor Kingdom, halfway you come across two paths to follow, one through a FOREST and another over the MOUNTAINS that are to the right of the forest.[FOREST/MOUNTAINS]").lower()

    if fight_forest_or_mountains == 'forest':
        forest_continue_or_investigate = input("\nWalking through this forest you notice that the day begins to darken, - “The night is coming”, you think, and you know what this can bring, in the darkness live evil and dangerous beings. After 1 hour towards the city and inside the forest you start to hear strange noises, and in a reflex, you stop your horse in the middle of the darkness of the forest, you almost fell into a trap of Globin. You can CONTINUE your way or INVESTIGATE the area for Globins.[CONTINUE/INVESTIGATE]").lower()

        if forest_continue_or_investigate == 'continue':
            print("\nYou then continue on your way and nothing else comes your way, you then arrive at the Fortfud royal family and hand them the talisman that was lost until then. They don't know how you managed to find it, but he thank you so much for getting the talisman and says that when they come back to power they will remember you!")
        elif forest_continue_or_investigate == 'investigate':
            print(f"\nYou then get off your horse and start looking for some clue where the Globins may be, but what you find amazes you, even more, you find the magician Martyst lying down, he looks like he's dead but you can still feel his breath, he then wakes up and looks at you and then says: - “{name}, do not give this talisman to the Fortfud family, they are not who you think they are, this talisman keeps the magic of the dark world safely trapped.. .”, he tries to say something more but ends up closing his eyes and dying... You then flee with the talisman to your mother city and hide the talisman, and never spoke about it again.")
        else:
            print(f"\nI don't know what {forest_continue_or_investigate} means")
    elif fight_forest_or_mountains == 'mountains':
        mountains_handle_or_escape = input("\nRiding through the mountain you can see that something is not right with the Ghusfor Kingdom, it looks like it is being surrounded, you then on the way to the Fortfud royal family meet your old master who stops you and says: - 'You are blind, that pride of yours. will make us all die, don't trust the Fortfud's, they're not who you think they are', but you don't listen to him very much, how can an old man like the one who abandoned his post of General to protect Martyst's daughter be talking the truth?\nYou then wonder whether to HANDLE the talisman or ESCAPE and investigate further into what is surrounding the realm.[HANDLE/ESCAPE]").lower()

        if mountains_handle_or_escape == 'handle':
            print("\nYou then continue on your way and nothing else comes your way, you then arrive at the Fortfud royal family and hand them the talisman that was lost until then. They don't know how you managed to find it, but he thank you so much for getting the talisman and says that when they come back to power they will remember you!")
        elif mountains_handle_or_escape == 'escape':
            print(f"\nYou run in the opposite direction of the Kingdom, and you end up in the dark forests, and then, lying on the ground, you find the magician Martyst lying there, he looks like he's dead but you can still feel his breath, he then wakes up and looks at you and then says: - “{name}, do not give this talisman to the Fortfud family, they are not who you think they are, this talisman keeps the magic of the dark world safely locked away...”, he tries to say more The thing but ending up closing your eyes and dying... You then run off with the talisman to your mother city and hide something from the talisman, and never spoke of it again.")
        else:
            print(f"\nI don't know what {mountains_handle_or_escape} means")
    else:
            print(f"\nI don't know what {fight_forest_or_mountains} means")
elif fight_or_run == 'run':
    run_forest_or_mountains = input("\nYou run towards your horse and get on it, when you start to run away, the mercenary draws a bow in arrow and shoots at you, but your horse is one of the fastest in the Kingdom, and he manages to dodge the arrows and soon the mercenary no longer has his sights on him. On the way towards the city of the Ghusfor Kingdom you come across two paths to follow, one through a FOREST and the other over the MOUNTAINS that are to the right of the forest.[FOREST/MOUNTAINS]").lower()

    if  run_forest_or_mountains == 'forest':
        forest_continue_or_investigate2 = input("\nWalking through this forest you notice that the day begins to darken, - “The night is coming”, you think, and you know what this can bring, in the darkness live evil and dangerous beings. After 1 hour towards the city and inside the forest you start to hear strange noises, and in a reflex, you stop your horse in the middle of the darkness of the forest, you almost fell into a trap of Globin. You can CONTINUE your way or INVESTIGATE the area for Globins.[CONTINUE/INVESTIGATE]").lower()

        if forest_continue_or_investigate2 == 'continue':
            print("\nYou then continue on your way and nothing else comes your way, you then arrive at the Fortfud royal family and hand them the talisman that was lost until then. They don't know how you managed to find it, but he thank you so much for getting the talisman and says that when they come back to power they will remember you!")
        elif forest_continue_or_investigate2 == 'investigate':  
            print(f"\nYou then get off your horse and start looking for some clue where the Globins may be, but what you find amazes you, even more, you find the magician Martyst lying down, he looks like he's dead but you can still feel his breath, he then wakes up and looks at you and then says: - “{name}, do not give this talisman to the Fortfud family, they are not who you think they are, this talisman keeps the magic of the dark world safely trapped.. .”, he tries to say something more but ends up closing his eyes and dying... You then flee with the talisman to your mother city and hide the talisman, and never spoke about it again.")
        else:
            print(f"\nI don't know what {forest_continue_or_investigate2} means") 
    elif run_forest_or_mountains == 'mountains':
        mountains_handle_or_escape2 = input("\nRiding through the mountain you can see that something is not right with the Ghusfor Kingdom, it looks like it is being surrounded, you then on the way to the Fortfud royal family meet your old master who stops you and says: - 'You are blind, that pride of yours. will make us all die, don't trust the Fortfud's, they're not who you think they are', but you don't listen to him very much, how can an old man like the one who abandoned his post of General to protect Martyst's daughter be talking the truth?\nYou then wonder whether to HANDLE the talisman or ESCAPE and investigate further into what is surrounding the realm.[HANDLE/ESCAPE]").lower()

        if mountains_handle_or_escape2 == 'handle':
            print("\nYou then continue on your way and nothing else comes your way, you then arrive at the Fortfud royal family and hand them the talisman that was lost until then. They don't know how you managed to find it, but he thank you so much for getting the talisman and says that when they come back to power they will remember you!")
        elif mountains_handle_or_escape2 == 'escape':
            print(f"\nYou run in the opposite direction of the Kingdom, and you end up in the dark forests, and then, lying on the ground, you find the magician Martyst lying there, he looks like he's dead but you can still feel his breath, he then wakes up and looks at you and then says: - “{name}, do not give this talisman to the Fortfud family, they are not who you think they are, this talisman keeps the magic of the dark world safely locked away...”, he tries to say more The thing but ending up closing your eyes and dying... You then run off with the talisman to your mother city and hide something from the talisman, and never spoke of it again.")
        else:
            print(f"\nI don't know what {mountains_handle_or_escape2} means")   
    else:
        print(f"\nI don't know what {run_forest_or_mountains} means")       
else:
    print(f"\nI don't know what {fight_or_run} means")       
        
