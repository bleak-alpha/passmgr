import dbman as db
import menu

menu.title()
while True:
    #Intro
    menu.menu()

    while True:
        c = input("Enter Your Choice: ")
        if c=='Q' or c=='q':
            break
        try:
            c = int(c)
        except:
            print("Please Enter a Numeric Value....")
            continue
        break

    if c==1:
        db.add()
        prompt = input("\nDo you want to return to Menu(M) or Quit(Q)?")
        if prompt=='M' or prompt=='m':
            continue
        if prompt=='Q' or prompt=='q':
            break

    if c==2:
        db.find()
        prompt = input("\nDo you want to return to Menu(M) or Quit(Q)?")
        if prompt=='M' or prompt=='m':
            continue
        if prompt=='Q' or prompt=='q':
            break

    if c==3:
        db.update()
        prompt = input("\nDo you want to return to Menu(M) or Quit(Q)?")
        if prompt=='M' or prompt=='m':
            continue
        if prompt=='Q' or prompt=='q':
            break
    
    if c==4:
        db.delete()
        prompt = input("\nDo you want to return to Menu(M) or Quit(Q)?")
        if prompt=='M' or prompt=='m':
            continue
        if prompt=='Q' or prompt=='q':
            break

    if c==5:
        db.showall()
        prompt = input("\nDo you want to return to Menu(M) or Quit(Q)?")
        if prompt=='M' or prompt=='m':
            continue
        if prompt=='Q' or prompt=='q':
            break

    break