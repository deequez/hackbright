from random import randint


print "Howdy, what's your name?"
name = raw_input()

print name + ", I'm thinking of a number between 1 and 100. Try to guess that number."

answer = randint(1,100)

count = 0

while True:
    guess = (raw_input("Your guess? "))
    count += 1     
    guess = int(guess) 

    if guess < answer:
        print "Your guess is too low, try again."
    elif guess > answer:
        print "Your guess is too high, try again."
    elif guess == answer:
        print "Well done, " + name + "! You found my number in %d tries!" % count
        break
    else:
        print "You didn't give us the right input, try again buddy!" 