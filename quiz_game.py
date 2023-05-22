import tkinter as tk
window = tk.Tk()
#tk.Tk().mainloop() # works the same as windows.mainloop()

main_label = tk.Label(
    text="Computer Quiz Game",
    #foreground='white',
    #background='black',
    #width="20",
    #height="15"
)

window.geometry("500x500")
"""
button = tk.Button(
    text="Click me",
    fg="black",
    bg="pink",
    height=5,
    width=10
)
"""
a_1 = tk.Entry()
q_1 = tk.Label(text="What does CPU stand for?").place(y=20, x=20)

a_2 = tk.Entry()
q_2 = tk.Label(text="What does GPU stand for?").place(y=40, x=20)
main_label.pack()
#button.pack(side="top")
a_1.pack()
a_2.pack()
name = a_1.get()
print(name)
window.mainloop()

"""
answer = input("Hello! Would you like to play the computer quiz game? ").lower()
if answer != 'yes':
    quit()

score = 0
answer = input('What does CPU stand for? ').lower()
if answer == 'central processing unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input('What does GPU stand for? ').lower()
if answer == 'graphics processing unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("You got {0} answer(s) correct.".format(str(score)))
print("You got {0}%.".format((score / 2) * 100))

# I wrote this line on Github website

"""