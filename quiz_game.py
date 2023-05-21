answer = input("Hello! Would you like to play the computer quiz game? ").lower()
if answer != 'yes':
    quit()

score = 0
answer = input('What does CPU stand for? ').lower()
if answer == 'central processing unit':
    print("Correct!")
    score += 1
    
answer = input('What does GPU stand for? ').lower()
if answer == 'graphics processing unit':
    print("Correct!")
    score += 1

print(score)
print("You got {0} answer(s) correct.".format(str(score)))
print("You got {0}%.".format((score / 2) * 100))

# I wrote this line on Github website
