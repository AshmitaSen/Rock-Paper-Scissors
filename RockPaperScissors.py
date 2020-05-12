import random
ls=['rock','paper','scissors']
def main():
    c=0
    u=0
    n=int(input("Max points:"))
    while c!=n and u!=n:
        comp=random.choice(ls)
        user=input("User: ")
        print("Computer:",comp)
        if (user=='rock'and comp=='paper') or (user=='paper' and comp=='scissors') or (user=='scissors' and comp=='rock'):
            c+=1
            print('Computer=',c)
            print('User=',u)
        elif (comp=='rock'and user=='paper') or (comp=='paper' and user=='scissors') or (comp=='scissors' and user=='rock'):
            u+=1
            print('Computer=',c)
            print('User=',u)
        else:
            print('Computer=',c)
            print('User=',u)
    if c>u:
        print("Winner is Computer with",c,"points")
    elif u>c:
        print("Winner is User with",u,"points")
    else:
        print("Draw")
if __name__=="__main__":
    main()
        
