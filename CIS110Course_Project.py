print("Greetings, Welcome to The Lost Puppy story.")
print("This story will detail an experience a lost puppy encountered while trying to make their way back home.")
print("To personalize this story, please answer the next few questions. Please press enter after each answer.")
input("Press the enter key to continue...")

print("*************")
userName = input("What is your name?:   ")
if userName.lower() == "dee":
    print("\nHello Queen, Welcome Back!")
else:
    print("\nSalutations!  " + userName +  " Welcome to The Lost Puppy Story!")
print("*************")

dogBreed = input("\nWhat breed is the lost dog?: ")
puppyName = input("\nWhat is the puppy name?: ")
capitalName = input("\nWhat is the capital of your state?: ")
parksName = input("\nWhat is the name of a dog park near you?:  ")
favoriteFood = input("\nWhat is your favoirte food?:  ")


print("*************")
print("So, " +userName+  " Are you ready to begin?  ")
print("**************")


print("This is an adventure of puppy who became lost while out on a stroll with it's owner.")
print("The puppy begins to panic as this has never happened before...Oh No! What shall I Do?")
print("The puppy begins to think......")

question_1 = input("\nShould " + (puppyName) + " the " + (dogBreed) +  ", go to the dogpark?  ")
if question_1.lower() == "yes":
   print("\nThe Lost Puppy, " +puppyName+ " wonders into the " +parksName+ " dogpark.")
   print("When the puppy notices that it doesn't smell the scent of its' owner.")
   print("That's when " +puppyName+ " begins to whimper as " +puppyName+ " was certain their owner would be there.")  
else:
    print("\nThe lost puppy was a "  +dogBreed+  " named "  +puppyName+ "  who encounters Danny the Doberman Pincher")
    print("before he passes  " +parksName+ ". " +puppyName+ "  decides to take another route....")
    print("bypassing the " +parksName+ "  dog park and goes over the bridge instead.")
    print("By taking this route,  " +puppyName+ " the " +dogBreed+ " avoids any conflict with Danny.")
    print("As  " +puppyName+ "  crosses the bridge they pick up on a familiar scent.....")

print("\n" + puppyName + " smells the scent of " + favoriteFood + " food stand" )
print("This place smells great!" + puppyName + " the " + dogBreed + " thinks. Hopefully, I will find my owner soon." )
print(" Just as, " + puppyName + ", begins to adopt a more positive attitude, things take a dramatic turn....")
print("\n**************")

question_2 = input("\nWill " + (puppyName) + " the " + (dogBreed) +  ", get caught by" + (capitalName) + ", Anmial Control?")
if question_2.lower() == "yes":
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
    print("After going down to " +capitalName+ " City Hall, where thier owner works.")
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