                                #'''HANGMAN GAME MADE BY ANIKET AND TESTING BY PRIYANSH'''
print("****************************************HANGMAN*******************************")
diction={1:"aniket",2:"priyansh",3:"chirag",4:"junaid",5:"sheikhmehreen"}
print("Enter the Players Name")
Player1=input()
Player2=input()
print("Who will guess the word ")
start=input()
if(start==Player1):
    setter=Player2
else:
    setter=Player1
print("Enter the number of chances")
chance=int(input())
print("{} set the word".format(setter))
n=int(input())
word=diction[n]
temp=word
flag=0
target=len(word)
while(chance>0):
    s=input("Enter an alphabet to guess that word:")
    if s in word:
        count=word.count(s)
        while s in word:
            word=word.replace(s,"")
        target-=count
        print("Target left:"+str(target))
        print("The guess alphabet is in the word")
    else:
        chance-=1
        print("It is not present inside the word")
    if(target==0):
        flag=1
        print("Yes you Won the game {}".format(start))
        break
    else:
        print("Attempts Remaining :"+str(chance))
if(flag==0):
    print("{} lose the game".format(setter))
    print("WORD IS:{}".format(temp))
else:
    print("WORD IS:{}".format(temp))

        
    

