print("Be sure to read ALL the directions. Type 'continue' and hit enter")
for i in range(3):
        decision=input()
        if decision=="continue":
            print("Would you play a game that made you make all the decisions? Type in 'yes' or 'no' and hit enter.")
        elif decision=="yes":
            print("Good. If bad things happened to your character when you made mean or bad decisions, do you think it could help you make better decisions. Be SURE to type 'could' or 'couldn't.")
        elif decision=="no":
            print("Okay. I see. Type why you said no.")
        elif decision=="could":
            print("Okay. Thank you for your feedback.")
        elif decision=="couldn't":
            print("Tell me why you say it couldn't help.")
        
print("Alright, I guess '"+input()+"' is a good answer.")
input()
