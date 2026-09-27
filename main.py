# -*- coding: utf-8 -*-
"""
Project name: Human Shazam
Student Number: s1122062 
Name: Levente Bódi

I declare that the work submitted here is from my authorship only. 
I haven’t used any generative AI to help with any code/text included in my work. 
I have given credit for the help I had conceptualizing my project. 
My work respects the university and course code of conduct.
"""
#I've just imported the libraries and modules I will need later on in the code
import winsound
import time
import random
import sys

#By here, I just declared a function, which writes out strings like in video games from character to character
#The  sys.stdout.write(i) writes a character from the string, without making a new line, the sys.stdout.flush() prints immediately on the console, so that the flow of characters will be continuous
#And, the time.sleep(0.1) waits 0.1 sec until the next character will be printed out
def kiiras(x):
    for i in x:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)


#By here I make sure, that the rounds of the game can be modified easily, so that tests can be run easily during the development phase 
var4=10

#Here, I explain the whole game, as it is explained in the project decription 

string="Now, dear User, we are going back to the era, when people had music taste, where songs started with an extremely recognizable opening; namely back to 2010's! "
kiiras(string)
string="I invite you to a game, where you should guess the song; AND for plus points the author. "
kiiras(string)
time.sleep(3)
string="The best 10 user will be on the podium, who you hopefully want to overscore. "
kiiras(string)
string="Before we start, I would like to ask you to give me your precious username: "
kiiras(string)

user_name=input()

string="Thank you very much, dear! "
kiiras(string)
string="I don't want to waste your time, so here are the rules: "
kiiras(string)
string="You will hear a song immediately after you press yes to the question 'Are you ready?'. "
kiiras(string)
time.sleep(3)
string="Then, you need to type in the name of the song, but only in LOWERCASE letters, spaces and if the name contains, special characters. "
kiiras(string)
string="After that you will be asked about the author; if you know them, type it too according to the rules mentioned for the name of the song. "
kiiras(string)
string="The song will stop after you typed in the answer for the song's name. " 
kiiras(string)
string="So, for example if you hear Stayin' Alive from Bee Gees (which will not happen, because we are in 2010's), then for the name of the song you should type 'stayin' alive' and for the author 'bee gees'. "
kiiras(string)
time.sleep(3)
string="You will only be asked ", str(var4), " songs, which you have to guess. "
kiiras(string)
string="You get 1000 points minus the time you spent for the name of the song, and you get 500 minus the time you spent on the name of the author. However, in case you can't guess or misstype them you will end up 0 points for that song/author " + '\n'
kiiras(string)
string="So, don't spend too much time on a song, because time counts, but rather guess than skipping it! "
kiiras(string)

var4=int(var4)

#Here, I make a list, in which I'll store the names of the songs
lista=[]

with open('top100.txt', 'r') as top100:
    for i in top100:
        lista.append(i.rstrip('\n'))





#Here, I make a list, in which I'll store the authors of the songs
lista2=[]

with open('top100eloado.txt', 'r') as top100eloado:
    for i in top100eloado:
        lista2.append(i.rstrip('\n'))
        
#sum1 will be the points of the user

sum1=0




 
for i in range (var4):
    
    #Here, we play the actual game. I ask the user till the point they are ready.
    ready="no"
    while (ready!="yes"):
        ready=input("Are you ready for the next song? [yes/no] ")
        
    #Here, I start time, and then later on I'll end it, and the end-start will be a deduction of the points
    start=time.time()
    
    #Here, I pick a random song from the lista, store the index in var2
    var1=random.choice(lista)
    var2=lista.index(var1)
    
    #Here, I play the chosen song in loop, and make sure, that the user can end it with an input, then I store the input and later on I make a comparison if the user guessed the song or not
    winsound.PlaySound(var1, winsound.SND_ASYNC + winsound.SND_LOOP)
    name_of_song=input("Enter the name of the song: ")
    winsound.PlaySound(None,0)
    
    #Here the time ends, and later end-start will be a deduction if points are gained
    end=time.time()
    
    #Here, I make a comparison if the user guessed the song, and also make sure, that they can't go in minus points, and after all, I add the points (if gained) to the users score
    if name_of_song==var1 and end-start>0:
        sum1=sum1+1000-(end-start)

    start=time.time()
    
    author_of_song=input("What is the name of the author?: ")
    
    end=time.time()
    
    #Here, I make a comparison if the user guessed the author of the song, and also make sure, that they can't go in minus points, and after all, I add the points (if gained) to the users score
    var2=int(var2)
    if author_of_song==lista2[var2] and end-start>0:
        sum1=sum1+500-(end-start)
        
    #Here I make sure with the pop() command, that the program won't play the same song in one game
    lista.pop(var2)
    lista2.pop(var2)
    
#Here I print some greeting and the score of the user on the screen
#print("It is the end of the game, " + user_name + ", thank you for playing with me!")
print("Your final score is " , round(sum1, 2) , "from ", var4*1500 , "you did a great job!")

#Here I use top10 and top10names for writing the scores and names in a separate file, and I also use lista3 and lista4 to be able to work with the content of the txt files inside of the program
lista3=[]
lista4=[]
marvolt=False
sum1=round(sum1, 2)
#Reading the files top10 and top10names
with open ("top10.txt", "r") as top10:
    for i in top10:
        lista3.append(i.rstrip('\n'))
        
        
with open ("top10names.txt", "r") as top10names:
    for i in top10names:
        lista4.append(i.rstrip('\n'))
#These lists are for containing temporarily the values of list3 and list4
lista5=[]
lista6=[]
for i in range (10):
    lista5.append(lista3[i])
    lista6.append(lista4[i])
#Modifying the files top10, top10names, and top10alltimes according to the user's score
for i in range(10):
    if sum1>float(lista3[i]) and marvolt==False:
        #By this I slide the list elements by one, in other words I make space for the new leaderboard winner
        for j in range (i, 9):
            lista5[j+1]=lista3[j]
            lista6[j+1]=lista4[j]
        lista3[i]=sum1
        lista4[i]=user_name
        for j in range (i, 9):
            lista3[j+1]=lista5[j+1]
            lista4[j+1]=lista6[j+1]
        marvolt=True
        
#just a preliminary testprint for the leaderboard before writing out to files
#for i in range(10):
    #print(lista4[i])  
    #print(lista3[i])       

with open ("top10.txt", "w") as top10:
    for i in range(10):
        top10.write(str(lista3[i]))
        top10.write('\n')
        
        
with open ("top10names.txt", "w") as top10names:
    for i in range(10):
        top10names.write(lista4[i] + '\n')

with open ("top10alltimes.txt", "w") as topall:
    
    for i in range (10):
        topall.write(lista4[i] + '\n')  
        topall.write(str(lista3[i]) + '\n')


#I write out if the user is on the toplist
if marvolt==True:
    string="You are also on the list! Good job!" + '\n'
    kiiras(string)
    

string="Here is a list of the 10 greatest players all time: " + '\n'
kiiras(string)



#Here, I write out inside of the program the names and scores of the 10 best players
for i in range(10):
    string=lista4[i] + '\n'
    kiiras(string)
    string=str(lista3[i]) + '\n'
    kiiras(string)
    



