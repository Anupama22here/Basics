from tkinter import *
import random
from tkinter import messagebox

#creating button
root=Tk()
root.title("Tic-Tac-Toe")

#x starts with true
start=True
count=0


    


#disabling buutons
def disable_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

#check for wins
def ifwon():
    global winner
    winner=False
    #checking possibilities for x
    if b1["text"]=='X'and b2["text"]=='X'and b3["text"]=="X":
        #change bg
        b1.config(bg='yellow')
        b2.config(bg='yellow')
        b3.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","X wins!")
        #disabling
        disable_buttons()
    elif b4["text"]=='X'and b5["text"]=='X'and b6["text"]=="X":
        #change bg
        b4.config(bg='yellow')
        b5.config(bg='yellow')
        b6.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","X wins!")
        #disabling
        disable_buttons()
    elif b7["text"]=='X'and b8["text"]=='X'and b9["text"]=="X":
        #change bg
        b7.config(bg='yellow')
        b8.config(bg='yellow')
        b9.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","X wins!")
        #disabling
        disable_buttons()
    elif b1["text"]=='X'and b5["text"]=='X'and b9["text"]=="X":
        #change bg
        b1.config(bg='yellow')
        b5.config(bg='yellow')
        b9.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","X wins!")
        #disabling
        disable_buttons()
    elif b3["text"]=='X'and b5[ "text"]=='X'and b7["text"]=="X":
        #change bg
        b3.config(bg='yellow')
        b5.config(bg='yellow')
        b7.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","X wins!")
        #disabling
        disable_buttons()
    elif b2["text"]=='X'and b5["text"]=='X'and b8["text"]=="X":
        #change bg
        b2.config(bg='yellow')
        b5.config(bg='yellow')
        b8.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","X wins!")
        #disabling
        disable_buttons()
    elif b1["text"]=='X'and b4["text"]=='X'and b7["text"]=="X":
        #change bg
        b1.config(bg='yellow')
        b4.config(bg='yellow')
        b7.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","X wins!")
        #disabling
        disable_buttons()
    elif b3["text"]=='X'and b6["text"]=='X'and b9["text"]=="X":
        #change bg
        b3.config(bg='yellow')
        b6.config(bg='yellow')
        b9.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","X wins!")
        #disabling
        disable_buttons()

#checking possibilities for o
    elif b1["text"]=='O'and b2["text"]=='O'and b3["text"]=="XO":
        #change bg
        b1.config(bg='yellow')
        b2.config(bg='yellow')
        b3.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","O wins!")
        #disabling
        disable_buttons()
    elif b4["text"]=='O'and b5["text"]=='O'and b6["text"]=="O":
        #change bg
        b4.config(bg='yellow')
        b5.config(bg='yellow')
        b6.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","O wins!")
        #disabling
        disable_buttons()
    elif b7["text"]=='O'and b8["text"]=='O'and b9["text"]=="O":
        #change bg
        b7.config(bg='yellow')
        b8.config(bg='yellow')
        b9.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","O wins!")
        #disabling
        disable_buttons()
    elif b1["text"]=='O'and b5["text"]=='O'and b9["text"]=="O":
        #change bg
        b1.config(bg='yellow')
        b5.config(bg='yellow')
        b9.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","O wins!")
        #disabling
        disable_buttons()
    elif b3["text"]=='O'and b5["text"]=='O'and b7["text"]=="0":
        #change bg
        b3.config(bg='yellow')
        b5.config(bg='yellow')
        b7.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","O wins!")
        #disabling
        disable_buttons()
    elif b2["text"]=='O'and b5["text"]=='O'and b8["text"]=="O":
        #change bg
        b2.config(bg='yellow')
        b5.config(bg='yellow')
        b8.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","O wins!")
        #disabling
        disable_buttons()
    elif b1["text"]=='O'and b4["text"]=='O'and b7["text"]=="O":
        #change bg
        b1.config(bg='yellow')
        b4.config(bg='yellow')
        b7.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","O wins!")
        #disabling
        disable_buttons()
    elif b3["text"]=='O'and b6["text"]=='O' and b9["text"]=="O":
        #change bg
        b3.config(bg='yellow')
        b6.config(bg='yellow')
        b9.config(bg='yellow')
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","O wins!")
        #disabling
        disable_buttons()
    
    #if ties
    if count==0 and winner==False:
        messagebox.showinfo("Tic-Tac-Toe","It's a tie\n No one wins")
        disable_buttons()

#this function intended to handle the click event for the buttons
def b_click(b):
    global start,count
    #This condition ensures that if the button has not been clicked before and it's the player's turn to play
    if b["text"]==" " and start==True:
        b["text"]="X"
        start=False
        count+=1
        ifwon()
    #not the player's turn
    elif b["text"]==" " and start==False:
        b["text"]='O'
        start=True
        count+=1
        ifwon()
    else:
        messagebox.showerror("Tic-Tac-Toe","That box has already been selected\n Please select another box:)")

def restart():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global start,count
    #tic tac toe has totally a count of 9 buttons so,
    b1=Button(root,text=" ",font=("Helvetica",25),height=4,width=7,bg='Silver',command=lambda:b_click(b1))
    b2=Button(root,text=" ",font=("Helvetica",25),height=4,width=7,bg='Silver',command=lambda:b_click(b2))
    b3=Button(root,text=" ",font=("Helvetica",25),height=4,width=7,bg='Silver',command=lambda:b_click(b3))

    b4=Button(root,text=" ",font=("Helvetica",25),height=4,width=7,bg='Silver',command=lambda:b_click(b4))
    b5=Button(root,text=" ",font=("Helvetica",25),height=4,width=7,bg='Silver',command=lambda:b_click(b5))
    b6=Button(root,text=" ",font=("Helvetica",25),height=4,width=7,bg='Silver',command=lambda:b_click(b6))

    b7=Button(root,text=" ",font=("Helvetica",25),height=4,width=7,bg='Silver',command=lambda:b_click(b7))
    b8=Button(root,text=" ",font=("Helvetica",25),height=4,width=7,bg='Silver',command=lambda:b_click(b8))
    b9=Button(root,text=" ",font=("Helvetica",25),height=4,width=7,bg='Silver',command=lambda:b_click(b9))

    #griding
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)
restart()
#creating menu
mymenu=Menu(root)
root.config(menu=mymenu)

options=Menu(mymenu,tearoff=False)
mymenu.add_cascade(label='Options',menu=options)
options.add_command(label="Reset game",command=restart)
root.mainloop()