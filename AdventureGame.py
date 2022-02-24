import sys

# Colors
black = "\x1b[1;30;47m"
yellow = "\x1b[1;33;47m"
green = "\x1b[1;32;47m"
blue = "\x1b[1;34;47m"
red = "\x1b[1;31;47m"
end = "\x1b[0m"
career = 0

# Introduction to Game (Done)
def intro():
    print(black + "* * * * * * \nJune 23, 2027 \n7:44 : \n    Orion 07 has successfully landed, and we have set foot on mars. This is a magnificent moment for all of us, and we hope the rest of humanity get to experience this feeling too. We have begun procedures to unpack the spaceship and we will contact you again shortly. Don't forget: One small step for man, a giant leap for humanity. \n* * * * * *" + end)
    next = input(green + "Press enter to continue:" + end)
    if next == "":
        print(black +  "* * * * * * \n    The message is 5 years old, the first, and last message sent from mars. It remains one of humanity's greatest triumphs, but at the same time... one of their greatest tragedies. \n    The disappearance of the 6 crew members on board was not taken lightly, but this year Orion 08 will be launched and finish what Orion 07 started. The primary objective of the mission will be to set up a hub where the first humans will be able to live. The secondary objective of the mission is to 'rescue' the missing crew of Orion 07, but the majority believe it's deliberate secondary objective is to retrieve the bodies of those lost. \n* * * * * *" + end)
        next0 = input(green + "Press enter to continue: " + end)
        if next0 == "":
            choice1()

# Choice 1 (Done)
def choice1():
    print(black + "* * * * * * \nApril 03, 2032 \n6:30 : \n    The mission starts in a few months time. You are a very experienced person, both as an astronaut and as a mission control crew. NASA invites you to take part in the mission as crew leader, so the space agency gives you a choice. \n* * * * * *" + end)
    next = input(green + "Press enter to continue:" + end)
    if next == "":
        print(yellow + "a: Become a member of the Orion 08 crew \nb: Become a mission control personnel" + end)
        choice = input(blue + "Make your choice: " + end)
        if choice == "a":
            astro()
        elif choice == "b":
            control()
        else:
            print(red + "Invalid choice, please retry" + end) 
            choice1()

# Astronaut (Done)
def astro():
    print(black + "* * * * * * \nAugust 09, 2032 \n21:33 : \n    4 months of preperation was complete, and the launch was scheduled for next week. The Orion 08 crew of 6 (Including you) have just gone to a restaraunt, as a way to celebrate their journey to mars, and as a way of waving the world goodbye. Your colleagues ask you if you need a drive home. \n* * * * * *"+ end)
    next = input(green + "Press enter to continue:" + end)
    if next == "":
        print(yellow + "a: Refuse and walk home\nb: Refuse and take a taxi\nc: Accept and drive home with your colleagues" + end)
        choice = input(blue + "Make your choice: " + end)
        if choice == "a":
            walk()
        elif choice == "b":
            taxi()
        elif choice == "c":
            drive()
        else:
            print("Invalid choice, please retry") 
            astro()
        
# Walk Home (Done)
def walk():
    print(black + "* * * * * * \n    You walk home slowly; feeling every step and every breath you take. You've been to space before, but never have you gone that far. This is your final week on earth before you see it again in months, maybe even years. The realization brings up a melancholy feeling. The ambience of distant cars, swaying trees, and the light emitted from street lights and buildings all feel so beautiful. You will miss this place.\n* * * * * *" + end)
    next = input(green + "Press enter to continue:" + end)
    if next == "":
        print(black + "* * * * * * \nThat same night... \n22:12 : \n    You've come home, sat down and started watching TV. Your phone vibrates in your pocket. It was a call from the agency... the other 5 crew members have gotten into a car accident; 1 has tragically passed away, 3 seriously injured, and 1 moderately injured. You felt adrenaile rush through your veins, followed by a sense of relief. You've known them for 4 months, but you never got too close with them. You were hoping the time on the spaceship would have brought you closer to them. The news still hurt you. However, you knew if you had gotten a ride home, it would be you among the victims, and you felt relieved, but guilty for feeling this way.\n* * * * * *" + end)
        next0 = input(green + "Press enter to continue:" + end)
        if next0 == "":
            print(black + "* * * * * * \nSeptember 14, 2032 \n12:30 : \n    The mission has been delayed by 6 months following the accident. Psychiatric assessments have determined the other 4 memebrs of your crew have developed mental issues, and has been disqualified from the mission. You on the other hand have not been diagnosed with any mental issues. You decide you will follow the mission through to the end, and your colleagues have recommended you to go to therapy.\n* * * * * *" + end)
            next0 = input(green + "Press enter to continue:" + end)
            if next0 == "":
                print(yellow + "a: Go to therapy\nb: Don't go to therapy" + end)
                choice = input(blue + "Make your choice: " + end)
                if choice == "a":
                    therapy()
                elif choice == "b":
                    notherapy()
                else:
                    print(red + "Invalid choice, please retry" + end) 
                    walk()

# Taxi ride home (Done)
def taxi():
    print(black + "* * * * * * \n    The taxi ride home is quick, only 10 minutes, but it felt like hours. Everything around you seemed to be moving in slow motion. You've been to space before, but never have you gone that far. This is your final week on earth before you see it again in months, maybe even years. The realization brings up a melancholy feeling. The ambience of distant cars, swaying trees, and the light emitted from street lights and buildings all feel so beautiful. You will miss this place.\n* * * * * *" + end)
    next = input(green + "Press enter to continue:" + end)
    if next == "":
        print(black + "* * * * * * \nThat same night... \n22:12 : \n    You've come home, sat down and started watching TV. Your phone vibrates in your pocket. It was a call from the agency... the other 5 crew members have gotten into a car accident; 1 has tragically passed away, 3 seriously injured, and 1 moderately injured. You felt adrenaile rush through your veins, followed by a sense of relief. You've known them for 4 months, but you never got to know them enough to call them 'close frinds'. You were hoping the time on the spaceship would have brought you closer to them. The news still hurt you. However, you knew if you had gotten a ride home, it would be you among the victims, and you felt relieved, but guilty for feeling this way.\n* * * * * *" + end)
        next0 = input(green + "Press enter to continue:" + end)
        if next0 == "":
            print(black + "* * * * * * \nSeptember 14, 2032 \n12:30 : \n    The mission has been delayed by 6 months following the accident. Psychiatric assessments have determined the other 4 memebrs of your crew have developed mental issues, and has been disqualified from the mission. You on the other hand have not been diagnosed with any mental issues. You decide you will follow the mission through to the end, and your colleagues have recommended you to go to therapy.\n* * * * * *" + end)
            next0 = input(green + "Press enter to continue:" + end)
            if next0 == "":
                print(yellow + "a: Go to therapy\nb: Don't go to therapy" + end)
                choice = input(blue + "Make your choice: " + end)
                if choice == "a":
                    therapy()
                elif choice == "b":
                    notherapy()
                else:
                    print(red + "Invalid choice, please retry" + end) 
                    taxi()
    
# Therapy (Done)
def therapy():
    print(black + "* * * * * * \nMay 19, 2033 \n17:30 : \n    As you exit the psychotherapy office, your eyes are yellow. You had cried. Months of therapy brought up trauma from your youth, but also made you realize the impact of the accident 6 months ago. The death of your colleague sent the other into a series of mental issues. You still visit the 4 survivors and talk to them as your therapist suggests. You've grown closer to them, and the more you care, the more tragic the accident becomes. For the one who lost their life that day, for the four that lost their dreams that day, you push yourself forward and promise them you will make the mission a success. \n* * * * * *" + end)
    next = input(green + "Press enter to continue:" + end)
    if next == "":
        spaceship()

# No therapy (Done)
def notherapy():
    print(black + "* * * * * * \nMay 19, 2033 \n20:30 : \n    You lay down in your backyard looking up at the sky. All the things that await you out in space fill you with excitement. Sometimes your mind drifts off thinking about your dead colleague, or the other astronauts who were disqualified. It was sad, but joi outweighted the little sorrow you felt. Only a week left until launch, you're ready for this. \n* * * * * *" + end)
    next = input(green + "Press enter to continue:" + end)
    if next == "":
        spaceship()

# Drive in colleagues car (Done)
def drive():
    print(black + "* * * * * * \nAugust 10, 2032 \n9:18 : \n    You wake up with a headache. Bright lights hit your eyes as you struggle to open them. Everything is so quiet except some sort of beeping sound. You're confused, anyone would be in this situation. Suddenly you hear a clicking sound, as if a door was opened, and then you hear it. A woman's voice says something in a worried tone, but somehow you can't make out what it is. As things become clearer and you fully wake up, you realize you're in a hospital, then the memories start pouring in.\n* * * * * *" + end)
    next = input(green + "Press enter to continue:" + end)
    if next == "":
        print(black + "* * * * * * \n    It happened so quickly. The panicked screaming, the bright light, the loud honking, and the impact. It was painless, as you were knocked out in an instant, but those few seconds were engraved into your head, not just physically, but into your memories. Every loud voice in the distant halls of the hospital, every thud, every flashing light, it all reminded you of that night and you always panicked. A month later and you were out of the hospital and had a psychiatric assessment. You were diagnosed with PTSD, and this, combined with your physical injuries disqualified you from the Orion 08 mission. \n    You find out that 1 of your crewmate has sadly passed away, 2 seriously injured, and 3, including you, were moderately injured. You fall into a deep depression. In the following months you had therapy, but it did not cure the pain you felt. You lost a friend, you lost your dream, and now you had no motivation for anything. Do you quit your job at NASA, or do you continue?\n* * * * * *" + end)
        next = input(green + "Press enter to continue:" + end)
        if next == "":
            print(yellow + "a: Quit job\nb: Continue working" + end)
            choice = input(blue + "Make your choice: " + end)
            if choice == "a":
                nojob()
            elif choice == "b":
                decade()
            else:
                print(red + "Invalid choice, please retry" + end) 
                drive()
    
# No Job (Done)
def nojob():
    print(black + "* * * * * * \October 20, 2033 \n1:30 : \n    It was a painful few months after the accident. You tried to recover both physically and mentally, but you made little progress. As you sit on your couch watching the TV, waiting for news about the Orion 08. The crew should have landed around 15 minutes ago, so their message should arrive now. Their message was a relief, it was a success! You felt happy and sad at the same time; that could have been you on mars. Trying to get rid of the thought you fall asleep. \n    A few hours later, you wake up to the TV still on, and the news channel is still going on about something. As you slowly wake up, all the rambling becomes clear. The Orion 08 crew has gone missing...\n* * * * * *" + end)
    next = input(green + "Press enter to continue:" + end)
    if next == "":
        outro()
    
# Decade after Orion 08 (Done)
def decade(): 
    if nocareer == "denied":
         print(black + "* * * * * * \October 20, 2033 \n1:30 : \n    It has been a painfully slow 5 months since the launch of Orion 08. As you sit on your couch watching the TV, waiting for news about the Orion 08. The crew should have landed around 15 minutes ago, so their message should arrive now. Their message was a relief, it was a success! You felt happy and sad at the same time; that could have been you on mars. Trying to get rid of the thought you fall asleep. \n    A few hours later, you wake up to the TV still on, and the news channel is still going on about something. As you slowly wake up, all the rambling becomes clear. The Orion 08 crew has gone missing...\n* * * * * *" + end)
    else:
        print(black + "* * * * * * \October 20, 2033 \n1:30 : \n    It was a painful few months after the accident. You tried to recover both physically and mentally, but you made little progress. As you sit on your couch watching the TV, waiting for news about the Orion 08. The crew should have landed around 15 minutes ago, so their message should arrive now. Their message was a relief, it was a success! You felt happy and sad at the same time; that could have been you on mars. Trying to get rid of the thought you fall asleep. \n    A few hours later, you wake up to the TV still on, and the news channel is still going on about something. As you slowly wake up, all the rambling becomes clear. The Orion 08 crew has gone missing...\n* * * * * *" + end)
    next = input(green + "Press enter to continue:" + end)
    if next == "":
        print(black + "* * * * * * \June 12, 2043 \n10:30 : \n    A decade has gone by as the world grieved for the loss of Orion 08. All missions were pushed back, and there was even a controversy about stopping mars missions altogether. No one could explain the dissapearance of both Orion 07 and 08; no one could guess. Finally this year, a new mission has been scheduled, and on that mission, is you. You may be 43 years old now, but you are still one of the best astronauts to live...\n* * * * * *" + end)
        next0 = input(green + "Press enter to continue:" + end)
        if next0 == "":
            global career
            career = "decade"
            spaceship()
    
# Mission Control (Done)
def control():
    print(black + "* * * * * * \nAugust 09, 2032 \n22:12 : \n    4 months of preperation was complete, and the launch was scheduled for next week. You try to fall asleep, but you can't take your mind off of the upcoming mission, and the past tragedy of Orion 07. You are sure the mission will be a success, after all, it's been 5 years, and things have changed since the mystery of 2027. However, there is a small part of your subconsiousness that can't help but worry that history will repeat itself.\n    As you lay in you bed, your phone rings, snapping you out of your deep imagination. The 6 members of Orion 08 crew has gotten into a car accident; 1 has sadly passed away on the spot, 2 seriously injured, and 3 moderately injured. You didn't know the crew members well, but it still pained you to hear this...\n* * * * * *" + end)
    next = input(green + "Press enter to continue:" + end)
    if next == "":
        print(black + "* * * * * * \n    September 14, 2032 \n12:30 : \n    As you sit in your office, NASA's mission contol manager enters and asks you in a sort of sorrowful but mannerly way. 'It has been decided that the mission is further delayed by 6 months. The accident has taken a heavy toll on the mental wellbeing of the 5 remaining crew members, and it has been decided that new crewmates will be picked for the mission. The board has requested you to join this new crew. It is your decision. \n* * * * * *" + end)
        next0 = input(green + "Press enter to continue:" + end)
        if next0 == "":
                print(yellow + "a: Accept the request \nb: Deny the request" + end)
                choice = input(blue + "Make your choice: " + end)
                if choice == "a":
                    global career
                    career = "control"
                    spaceship()
                elif choice == "b":
                    global nocareer
                    nocareer = "denied"
                    decade()
                else:
                    print(red + "Invalid choice, please retry" + end) 
                    control()

# On the spaceship (Done)
def spaceship():
    if career == "control":
        print(black + "* * * * * * \nMay 26, 2033 \n10:30 : \n    'T minus 3, 2, 1, take off!' You listen to mission control through your radio. The spaceship shakes violently and lifts off into the sky. You close your eyes and try to control your breathing as you try to tolerate the G-force. Mission control will control the spacecraft for now, so all you can do is wait. The other astronauts next to you cheer as time passes. You cheer too, and in your mind you think; 'See you later, Earth. And see you soon, mars...'\n* * * * * *" + end)
    if career == "decade":
        print(black + "* * * * * * \nNovember 01, 2043 \n10:30 : \n    'T minus 3, 2, 1, take off!' You listen to mission control through your radio. The spaceship shakes violently and lifts off into the sky. You close your eyes and try to control your breathing as you try to tolerate the G-force. Mission control will control the spacecraft for now, so all you can do is wait. The other astronauts next to you cheer as time passes. You cheer too, and in your mind you think; 'See you later, Earth. And see you soon, mars...'\n* * * * * *" + end)
    else:
        print(black + "* * * * * * \nMay 26, 2033 \n10:30 : \n    'T minus 3, 2, 1, take off!' You listen to mission control through your radio. The spaceship shakes violently and lifts off into the sky. You close your eyes and try to control your breathing as you try to tolerate the G-force. Mission control will control the spacecraft for now, so all you can do is wait. The other astronauts next to you cheer as time passes. You cheer too, but not for the same reason as the others. You cheered because you will carry out the dream that the others couldn't fulfill. You thought of a deceased friend. You thought of your broken friends. See you later, old colleagues. See you later, Earth. And see you soon, mars...\n* * * * * *" + end)
    next = input(green + "Press enter to continue:" + end)
    if next == "":
        print(black + "* * * * * * \n    5 months on a spceship with 5 other people is often very boring. Astronauts can bring personal items with them, and some items are provided by NASA themselves to keep the atsronauts sane. However, due to the large amount of cargo on the ship, astronauts can only bring very a limited amount of items. What items did you bring with you? \n* * * * * *" + end)
        next1 = input(green + "Press enter to continue:" + end)
        if next1 == "":
            global item
            print(yellow + "a: Books + Notebook + Pencils + Game console\nb: Books + Camera + Music Player\nc: Books + Guitar + Movie CD's" + end)
            choice = input(blue + "Make your choice: " + end)
            if choice == "a":
                arrive()
                item = "game"
            elif choice == "b":
                arrive()
                item = "camera"
            elif choice == "c":
                arrive()
                item = "guitar"
            else:
                print("Invalid choice, please retry") 
                spaceship()

# Arrive on mars
def arrive():
    if career == "decade":
        print(black + "* * * * * * \nMay 08, 2043 \n00:30 : \n    The spaceship vibrates violently as it positions itself for landing. You brace yourself for heavy impact, but it was not as bad as you expected. You send a message back to earth, which would roughly take 15-20 minutes to reach them, and another 15-20 for their message to reach you. Okay, the landing was successful, but the real challenges are yet to come. The Orion 08 spaceship is around 38 km away from you and you will have to visit it sooner or later. The automatic cargo unloading will begin shortly; it will take some time. \n* * * * * *" + end)
    else:
        print(black + "* * * * * * \nSeptember 04, 2033 \n03:40 : \n    The spaceship vibrates violently as it positions itself for landing. You brace yourself for heavy impact, but it was not as bad as you expected. You send a message back to earth, which would roughly take 15-20 minutes to reach them, and another 15-20 for their message to reach you. Okay, the landing was successful, but the real challenges are yet to come. The automatic cargo unloading will take some time. \n* * * * * *" + end)
    next = input(green + "Press enter to continue:" + end)
    if next == "":
        print(black + "* * * * * * \n    In the meantime, you can wait on the ship, or you can take a rover and explore the area.\n* * * * * *" + end)
        next1 = input(green + "Press enter to continue:" + end)
        if next1 == "":
                print(yellow + "a: Wait on the ship \nb: Explore the surrounding area on a mars rover" + end)
                choice = input(blue + "Make your choice: " + end)
                if choice == "a":
                    waitship()
                elif choice == "b":
                    explore()
                else:
                    print("Invalid choice, please retry") 
                    spaceship()
            
# Explore the area on mars
def explore():
    if career == "decade":
        print(black + "* * * * * * \n    You take the rover with another crewmate and decide to visit the Orion 08 Spaceship. It was there as if it hadn't moved an inch. Covered in dust, the ship had been unloaded. The cargo was almost all covered in sand. You check through the resources and discover that most of it was still usable. Then you aproach the ship, prying the door open. The inside was clean, untouched by any dust. As you wanter around, there are books, bits and pieces of metal, clothes, and even food scattered throughout. Questions flood your head. What happened here? Why did it happen? Then you find a camera. You click the 'on' button several times, waiting several minutes, until you're hit with dim light. Surprisingly, there is already a video selected and you let it play. \n* * * * * *" + end)
        next = input(green + "Press enter to continue:" + end)
        if next == "":
            print(black + "* * * * * * \n    The camera is pointed outside the foggy window. It's somewhat dark, but the thin atmosphere of Mars made it brighter than 'dark' on Earth. Out in the distance, a rover speeds toward the ship, blowing up dust in it's path. It's an unusual speed to be driving at, especially when you get this close to the ship. As the rover passes the view at an incredible speed, the camera is dropped. It shows people moving around, as if in a panick, and then everything is suddenly still. It lays still for 17 more minutes and the video stops at exactly the 30 minute mark...\n* * * * * *" + end)
            next2 = input(green + "Press enter to continue:" + end)
            if next2 == "":
                outro()
    else:
        print(black + "* * * * * * \n    You take the rover with another crewmate and decide drive to a nearby hill to set up an antenna. The nearest hill was 20 km away, and without a doubt, it was much larger than those on Earth. After you set up the antenna, a small dust-storm begins to form, making the distance barely visible. You and your other crewmate decide to drive into a dave located downhill. It was dark, almost pitch black. The dust-storm made it worse as dust particles on your helmet made even bright things hard to look at. As the dust-storm begins to fade away and everything quiets down, the ground begins to shake violently. Barely keeping your balance, you and your partner get into the rover and try to move slowly away from the cave. About a minute passes, you are far from the cave, and the earthquake stops. Suddenly the rover accelerates at an abnormal rate. The spaceship comes into view quickly, and before you know it, you are already past it. Not a second later and the rover halts, knocking you out...\n* * * * * *" + end)
        next1 = input(green + "Press enter to continue:" + end)
        if next1 == "":
            outro()
    
# Wait in the spaceship
def waitship():
    print(black + "* * * * * * \n    2 of your crewmates take a rover to go set up an antenna on a hill. You wait in your ship for the cargo to be unloaded. A couple minutes pass and suddenly a dust strom begins. It's hard to see anything outside, but when it clears, you see a large path of dust in the distance. A crewmate of yours brings out a camera and starts recodring. As a few seconds pass, it becomes clear that it is a rover in the distance. Suddenly the rover accelerates at an abnormal rate. The rover comes close very quickly, and before you know it, it is are already past the ship. Quickly, everyone stops everything they are doing, dropping everything and rushes to wear their spacesuits. You and the 2 remaining crewmates exit the spaceship and find that the rover had come to a stop not too far from here. You walk as carefully as you can to the rover. As you are just a few steps away from rover, everything suddenly turns pitch black. You can hear your crewmates panic, then everything is quiet, and then you lose conciousness... \n* * * * * *" + end)
    next = input(green + "Press enter to continue:" + end)
    if next == "":
        outro()

def outro():
    print(black + "* * * * * * \n    TO BE CONTINUED...\n* * * * * *" + end)
    sys.exit()
    
intro()
