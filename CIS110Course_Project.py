import sys
import time
def slowprint(string):
    for char in range(len(string)):
        print(string[char], end="")
    time.sleep(2./35)

slowprint("Greetings, Welcome to The Lost Puppy story.")
slowprint("This story will detail an experience a lost puppy encountered while trying to make their way back home.")
slowprint("To personalize this story, please answer the next few questions. Please press enter after each answer.")
input("Press the enter key to continue...")

print("*************")
userName = input("What is your name?:   ")
while (len(userName) == 0):
    userName = input("Wait! Please enter your name to move forward.:  ")
if userName.lower() == "dee":
    slowprint("\nHello Queen, Welcome Back!")
else:
    slowprint("\nSalutations!  " + userName +  " Welcome to The Lost Puppy Story!")
print("*************")

keepGoing = "y"
while keepGoing.lower() == "y":
            dogBreed = input("\nWhat breed is the lost dog?: ")
            puppyName = input("\nWhat is the puppy name?: ")
            capitalName = input("\nWhat is the capital of your state?: ")
            parksName = input("\nWhat is the name of a dog park near you?:  ")
            favoriteFood = input("\nWhat is your favoirte food?:  ")
            print("*************")
            slowprint("So, " + userName +  " Are you ready to begin?  ")
            print("**************")


            slowprint("This is an adventure of puppy who became lost while out on a stroll with it's owner.")
            slowprint("The puppy begins to panic as this has never happened before...Oh No! What shall I Do?")
            slowprint("The puppy begins to think......")

            question_1 = input("\nShould " + (puppyName) + " the " + (dogBreed) +  ", go to the dogpark?  ")
            if question_1.lower() == "yes":
               while question_1.lower() != "yes" and question_1.lower() != "no":
                    question_1 = input("That is not a valid value. Please enter your answer. Please only enter yes or no. ")
            while (len(question_1) ==0):
                question_1 = input("Hold on! The question cannot be left blank. Please enter yes or no.:")
                if question_1 == "yes":
                    slowprint("\nThe Lost Puppy, " +puppyName+ " wonders into the " +parksName+ " dogpark.")
                    slowprint("When the puppy notices that it doesn't smell the scent of its' owner.")
                    slowprint("That's when " +puppyName+ " begins to whimper as " +puppyName+ " was certain their owner would be there.")  
                else:
                    slowprint("\nThe lost puppy was a "  +dogBreed+  " named "  +puppyName+ "  who encounters Danny the Doberman Pincher")
                    slowprint("before he passes  " +parksName+ ". " +puppyName+ "  decides to take another route....")
                    slowprint("bypassing the " +parksName+ "  dog park and goes over the bridge instead.")
                    slowprint("By taking this route,  " +puppyName+ " the " +dogBreed+ " avoids any conflict with Danny.")
                    slowprint("As  " +puppyName+ "  crosses the bridge they pick up on a familiar scent.....")

            slowprint("\n" + puppyName + " smells the scent of " + favoriteFood + " food stand" )
            slowprint("This place smells great!" + puppyName + " the " + dogBreed + " thinks. Hopefully, I will find my owner soon." )
            slowprint(" Just as, " + puppyName + ", begins to adopt a more positive attitude, things take a dramatic turn....")
            slowprint("\n**************")

            question_2 = input("\nWill " + (puppyName) + " the " + (dogBreed) +  ", get caught by" + (capitalName) + ", Anmial Control?")
            if question_2.lower() == "yes":
                while question_2.lower() != "yes" and question_2.lower() != "no":
                    question_2 = input("That is not a valid value. Please enter your answer. Please only enter yes or no. ")
            while (len(question_2) == 0):
                question_2 = input("Hold on! The question cannot be left blank. Please enter yes or no.:")
            if question_2 == "yes":
                    print("\nAs,  " +puppyName+ "  the  " +dogBreed+  " continues over the bridge in,  " +parksName+ " they decide to purchase")
                    print("food at the " +favoriteFood+ " food stand.")
                    print("However,..." +puppyName+ "  is a little hesitant as they remeber that " +capitalName+ " has a strict rule")
                    print("against " +dogBreed+ " that are not accompained by an owner.")
                    print("Just as " +puppyName+ " began to weep, a stern voice yelled!...")
                    print("HEY YOU!, it was the head chief for, "  + capitalName + " Animal Control "+ puppyName + " decides to surrender...")
                    print("\n***************")
            else:          
                 print("\n" + puppyName + " the " + dogBreed + " decides to continue over the drawbridge,")
                 print("eluding " + favoriteFood + ", food stand. Eventhough, this is where thier owner usually stops by on thier daily walks.")
                 print("As, " + puppyName + " got closer to, " + favoriteFood + " food stand, a familair voice is heard.....")

            question_3 = input("\nWill you help " + (puppyName) + " The " + (dogBreed) +  ", find thier owner  " + (userName) + " , in the big city of " + capitalName + " ?")
            if question_3.lower() == "yes":
                while question_3.lower() != "yes" and question_3.lower() != "no":
                    question_3 = input("That is not a valid value. Please enter your answer. Please only enter yes or no. ")
            while (len(question_3) == 0):
                question_3 = input("Hold on! The question cannot be left blank. Please enter yes or no.:")
            if question_3 == "yes":
                    print("\nAfter going down to " +capitalName+ " City Hall, where thier owner works.")
                    print("To no avail, " +puppyName+ " the " +dogBreed+ " decides to see if they can make their way back home before the sunsets.")
                    print("As,  " +puppyName+ " is halfway through the city of " +capitalName+ " they remember")
                    print("that " +parksName+ " Animal Control will be able to locate thier owner with thier puppytag.")
                    print("Anmial Control at " +parksName+ " was able call the owner and " +puppyName+ " is estatic!")
            else:
              print("\n " + puppyName + ", the " + dogBreed + " has been trying to find their way home from," + parksName + " dog park since they were seperated from thier owner...")
              print("It has been over three hours and," + puppyName + " begins to give up on making it home before the sun sets.")
              print(" As soon as " + puppyName + " tucks his tail before beginning to look for shelter, a familar voice is heard.....")
              print("Apprehensive at first, " + puppyName + " notices that it's the next door neighbor.")
              print("\n " + puppyName + " the " + dogBreed + " jumps in the bed of the pickup relived to finally be on the way back home safely!")

              print("\n----------------")
              print("Thank You," +userName+ "for helping" +puppyName+ "find their way back home.")
              print("I hope you have enjoyed this adventure as much as I did!")
              print("You are awesome!")

              print("Would you like to go on another adventure with me? I'll set a timer to give you a minute to think...")

              for min in range(2, 1, -1):
                  print(min, "minutes remaining")
                  for seconds in range(60, 0, -1):
                      print(seconds, end = " \r")
                      import time
                      time.sleep(1)

slowprint("Ding! Time's Up!!!!!")

keepGoing = input("Would you like to go on another adventure? Enter yes or no:  ")