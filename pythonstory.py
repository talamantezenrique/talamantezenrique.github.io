import time
print("This is an adventure! Would you like to play?")
response=input()

if response=='yes' or response=='y':
    print ("Great! Let's get started")
    game = True
else:
    print("Ok, goodbye!")
    
    

if game==True:
        print("Left or Right? (left/right) ?")
        response=input()
        if response=='left':
            print ("You decide to go left. You come across an abandoned", '\n'
                   "old house. Do you go inside? (yes/no)")
            response=input()
            if response=='yes':
                    print("You walk into the abandoned house immediately notice a disgusting smell coming", '\n'
                              "from the upstairs of the house. It is so bad you almost feel the urge to vomit", '\n'
                              "Do you walk upstairs the house and investigate the smell? (yes/no)")
                    response=input() 
                    if response=='yes':
                        print("You walk upstairs the house and notice the smell is coming from the upstairs bathroom. You walk into the bathroom and see a zombie in the bathroom. He jumps on you and begins to maul you")
                        print("You are dead")
                    elif response=='no':
                        print("You decide not to investigate the smell and you walk into the kitchen of the house. You open the pantry")
                        print("You take out a box of cheerios and pour it into a bowl. You pour milk into the bowl and grab a spoon.")
                        print("You take a spoonfull of cheerios into your mouth. All of a sudden, you feel nauseous and you fall to the floor")
                        print("You are dead.")
            elif response=='no':
                    print("You walk past the abandoned house and into a street. You walk down the street for about", '\n'
                              "a mile, until you see your home. Do you go inside your home and go to bed? (yes/no)")
                    response=input()
                    if response=="yes":
                        print("You unlock your front door, walk in, and put your coat on the coat hanger. You take off your shoes and immediately walk up the stairs. You open your room door and then you crawl into your bed.")
                        print("Goodnight")
                    if response=="no":
                        print("You decide to walk past your home instead of going to bed. You continue walking down the same road you were already walking down. All of a sudden, you hear a honking sound. You turn around in a split second and see a red F150 with nitro turbo boosters and a can of nos in the back about to smack you at 90 mph. The truck hits you and you fly 60 feet into the air.")
                        print("You impact the ground. You are dead")
                    
                    
        if response=='right':
            print ("You decide to go right. You see an alley and begin", '\n'
                   "to walk down it. You find a note on the ground.", '\n'
                   "Do you pick up the note? (yes/no)")
            response=input()
            if response=='yes':
                    print('You pick up the note and you read it')
                    time.sleep(2)
                    print("Walk over to the garbage can to your right. Tip it over and look under the can. You will find a 100 round drum magazine next to an AK-47. Take the AK to the house at 1391 Flag Road and go to the bathroom.")
                    time.sleep(3)
                    print("Do you listen to the note, take the AK, and go to the address? (yes/no)")
                    response=input()
                    if response=='yes':
                            print("You take the AK, load it, and put a round in the chamber. You walk to the address and kick the door down. You run upstairs and immediately notice an atrocious smell. You run to the bathroom, kick the door down, and spot a zombie in the bathroom. You immediately unload your drum magazine into the zombie, killing it")
                            print("You win!")
                    if response=='no':
                            print("You walk past the AK and instead call the police. When the police arrive, they order you to put your hands up. When you put your hands up, they shoot you anyway")
                            print("You are dead")
                    
            elif response=='no':
                    print("You walk down the alley and turn down the right into an empty street. Your stomach begins to", '\n'
                          "growl and you notice you are hungry. You spot a McDonald's right across the street. Do you go there to eat?(yes/no)")
                    response=input()
                    if response=="yes":
                        print("You walk into the McDonald's and go to the front counter. You are greeted by a cashier named Felicia Bonquisha. She asks, 'what u finna eat.' You explain to her that you would like to have an ice cream cone. Felicia says, 'ice cream machine broke'. You then ask for her manager. Felicia responds with")
                        print(", 'manager machine broke'. At this point, you begin to boil with rage. You ball up your fist and punch Felicia in her face. She falls to the floor. You vault over the counter and steal 3 big macs and run out. As you are running out you hear someone yelling world star! in the back. You run home and sit on your front porch, eating the big macs, laughing about how you punched that thot in the face")
                    if response=="no":
                        print("You decide McDonald's isnt the wisest place to eat right now. You instead, walk to the nearby Jack in the Box for a nice munchy meal. As you are walking there, 3 men pull up in an all black cadillac and shoot you in the head")
                        print("You are dead")
        
