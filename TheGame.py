one='Hello. You live on a farm. Everyday, you are sent by your mother to get water. One day, as you are getting water, you see an old man. You can talk to him by typing "talk", or you can type "ignore" to ignore him.'

two=['The old man says he has a task for you. Type "accept" to accept or "decline" to decline', 'You walk home having ignored the old man. Your mom is mad. She tells you to go back and see what he had to say. Type "go" to go back or "resist" to resist her.']

three=['"Okay," says the old man. "I need you to go into the forest and find the most beautiful piece of wood you can find for me to carve. It could be dangerous, take this sword!" Type "no_sword" to leave the sword, or "sword" to take the sword.', '"Are you sure you would not like a little excitement?" said the old man. Type "I_am_sure" to decline, or "okay_fine" to change your mind.', 'Your mom is mad. She grounds you. You go to your room. You can choose to escape by typing "escape" or "stay" to stay in your room.']

four=['You head into the forest. As you are walking, you spot a beautiful piece of birch wood ahead of you. You grab the wood, but then realize it could be worth something if you sold it. Type "keep" to keep the valuable wood, or type "give" to bring it back to the old man.', 'You walk back home, and your mom is angry. She says you should respect elders. You can "go" and do the chore of the old man, or you can "resist" your mom.', 'You decided to escape. You make a rope of bedsheets, and climb out the window. You can run to the "forest" or the "town"', 'Your mom comes up to talk to you. You are in big trouble. You are then sent to boarding school. On the way, you escape! You decide that you need to run a way to an adventure! Will you go to the "tall_mountains", or the "dark_forest"?']

five=['Since you chose to keep the birch, you can not go back by way of the old man. You can escape to the "swamp" or deeper into the "woods".', 'You bring the piece of birch wood back to the old man. He is very happy with you, and lets you keep the sword. It will come in handy in the many adventures you will have. For you first adventure, will you go to the "tall_mountains", or the "dark_forest"?', 'In the forest, you see a beautiful piece of birch wood. Do you "take_it" or "leave_it"?', 'You head to the village. You have nowhere to go now, and you decide you have two options. You can run away with the "circus", or join a local "gang".']

six=['You arrive at the swamp. After walking around a while, you realize you are lost. You can keep on walking around by typing "walk" or you can try to "find" you way back.', 'As you go deeper into the woods, you here a rustling. A monster pops out! Do you have a sword? "yes" or "no".', 'You chose to take the birch! As you are walking home, you see a poor man. You can "let_him_have_it" or you can "keep_walking" and ignore him.', 'You chose to leave the birch! You go home empty handed! You decide that an adventure is what you need! Will you go to the "tall_mountains", or the "dark_forest"?', 'In the circus, you must choose an act. There are two open. You can be a "juggler", or a "clown".', 'In the gang, you are made a henchman "will_you" or "will_you_not" take this!']

seven=['You keep walking. You become lost. You decide you need to go some where you can see. Will you go to the "tall_mountains", or the "dark_forest"?', 'You eventually find your way home, but you are not satisfied. Something feels wrong, like it was something you did. Anyway, seems like a good time for an adventure! Will you go to the "tall_mountains", or the "dark_forest"?', 'The old man gave you a fake sword! Now you do not have a sword and the monster takes captive! Out of instinct you escape from the monster. Will you go to the "tall_mountains", or the "dark_forest"?', 'Now you do not have a sword and the monster takes captive! Out of instinct you escape from the monster. Will you go to the "tall_mountains", or the "dark_forest"?', 'Because you gave the poor man the birch, he turned his life around, became rich, and shared it with your family. With your home life secured, you go on an adventure. Will you go to the "tall_mountains", or the "dark_forest"?', 'The poor man becomes a leader of the town, eventually, and gets you evicted! Now you are poor!', 'You decided to be a juggler. As a juggler, you have to practice. If you "practice", you will get good at juggling! If you do not practice, you can not get better, and will be "fired"!', 'You decided to be a clown, but you are not very funny! You must "practice", if you do not want to be "fired"', 'You will not take this! You run away to an adventure! Will you go to the "tall_mountains", or the "dark_forest"?', 'You put up with the gang, until you fnally rebel. The gang is exploiting you too much. You decide to go on an adventure. Will you go to the "tall_mountains", or the "dark_forest"?'] 

eight=['You become successful in the circus. In your old age, you retire, and go on adventures. Will you go to the "tall_mountains", or the "dark_forest"?', 'You were fired from the circus. Now, you want to go on an adventure. Will you go to the "tall_mountains", or the "dark_forest"?', ]

newAdventure=[]

print(one)
while True:
        decision=input()
        sword=False
        
        if decision=="talk":
            print(two[0])
            decision=input()
            if decision=="accept":
                print(three[0])
                decision=input()
                if decision=="sword":
                    print(four[0])
                    decision=input()
                    if decision=="keep":
                        print(five[0])
                        decision=input()
                        if decision=="swamp":
                            print(six[0])
                            decision=input()
                            if decision=="walk":
                                print(seven[0])
                                decision=input()
                            elif decision=="find":
                                print(seven[1])
                                decision=input()
                        elif decision=="woods":
                            print(six[1])
                            decision=input()
                            if decision=="yes":
                                print(seven[2])
                                decision=input()
                            elif decision=="no":
                                print(seven[3])
                                decision=input()
                    elif decision=="give":
                        print(five[1])
                        decision=input()
                elif decision=="no_sword":
                    print(four[0])
                    decision=input()
                    if decision=="keep":
                        print(five[0])
                        decision=input()
                        if decision=="swamp":
                            print(six[0])
                            decision=input()
                        elif decision=="woods":
                            print(six[1])
                            decision=input()
                            if decision=="yes":
                                print(seven[2])
                                decision=input()
                            elif decision=="no":
                                print(seven[3])
                                decision=input()
                            if decision=="walk":
                                print(seven[0])
                                decision=input()
                            elif decision=="find":
                                print(seven[1])
                                decision=input()
                    elif decision=="give":
                        print(five[1])
                        decision=input()
            elif decision=="decline":
                print(three[1])
                decision=input()
                if decision=="okay_fine":
                    print(three[0])
                    decision=input()
                    if decision=="sword":
                        print(four[0])
                        decision=input()
                    elif decision=="no_sword":
                        print(four[0])
                        decision=input()
                elif decision=="I_am_sure":
                    print(three[2])
                    decision=input()
                    if decision=="escape":
                        print(four[2])
                        decision=input()
                        if decision=="forest":
                            print(five[2])
                            decision=input()
                            if decision=="take_it":
                                print(six[2])
                                decision=input()
                                if decision=="let_him_have_it":
                                    print(seven[4])
                                    decision=input()
                                if decision=="keep_walking":
                                    print(seven[5])
                                    decision=input()
                            elif decision=="leave-it":
                                print(six[3])
                                decision=input
                        elif decision=="town":
                            print(five[3])
                            decision=input()
                    elif decision=="stay":
                        print(four[3])
                        decision=input()
        elif decision=="ignore":
            print(two[1])
            decision=input()
            if decision=="go":
                print(three[0])
                decision=input()
                if decision=="sword":
                    print(four[0])
                    decision=input()
                    if decision=="keep":
                        print(five[0])
                        decision=input()
                        if decision=="swamp":
                            print(six[0])
                            decision=input()
                        elif decision=="woods":
                            print(six[1])
                            decision=input()
                            if decision=="yes":
                                print(seven[2])
                                decision=input()
                            elif decision=="no":
                                print(seven[3])
                                decision=input()
                            if decision=="walk":
                                print(seven[0])
                                decision=input()
                            elif decision=="find":
                                print(seven[1])
                                decision=input()
                    elif decision=="give":
                        print(five[1])
                        decision=input()
            elif decision=="resist":
                print(three[2])
                decision=input()
                if decision=="escape":
                        print(four[2])
                        decision=input()
                        if decision=="forest":
                            print(five[2])
                            decision=input()
                            if decision=="take_it":
                                print(six[2])
                                decision=input()
                                if decision=="let_him_have_it":
                                    print(seven[4])
                                    decision=input()
                                if decision=="keep_walking":
                                    print(seven[5])
                                    decision=input()
                            elif decision=="leave-it":
                                print(six[3])
                                decision=input
                        elif decision=="town":
                            print(five[3])
                            decision=input()
                            if decision=="circus":
                                print(six[4])
                                decision=input()
                                if decision=="juggler":
                                    print(seven[6])
                                    decision=input()
                                    if decision=="practice":
                                        print(eight[0])
                                        decision=input()
                                    elif decision=="fired":
                                        print(eight[1])
                                elif decision=="clown":
                                    print(seven[7])
                                    decision=input()
                            elif decision=="gang":
                                print(six[5])
                                decision=input()
                                if decision=="will_you":
                                    print(seven[9])
                                    decision=input()
                                elif decision=="will_you_not":
                                    print(seven[8])
                                    decision=input()
                elif decision=="stay":
                    print(four[3])
                    decision=input()
        
        if decision=="tall_mountains":
            print('Dat da end fo now!')
        elif decision=="dark_forest":
            print('Dat da end fo now!')
                             
input()