print (2+2)
#4

print(50 - 5*6)
#20

print(50 - 5*6 / 4)
#42.5

print(8 / 5)
#1.6

print("---------------------------")

print (17/3)
#druckt einen float

print(17//3)
#druckt ein int

print(17%3)
#druckt den rest der division

print(5*3+2)

print("---------------------------")

print(5**2)
#5 hoch 2

print(2**7)
#2 hoch sieben

print("---------------------------")

width=20
height=120
print(width*height)

print("---------------------------")

print(int(4*3.75-1))

print("---------------------------")

#number1=(input("Width: "))
#number2=(input("Height: "))
#print(int(number1)*int(number2))

print("---------------------------")

print("I don\"t!")
print("I don't!")
print("She said she doesn\"t")
print("She said she doesen't")

print("---------------------------")

s = "first line. \nSecond line."
print(s)

print("---------------------------")

print("Some \name")
print(r"Some \name")

print("---------------------------")

print("""
      
Name:             David
Age:              17
Location:         Germany
      
""")

print("---------------------------")

text= "Hallo "+"Welt"
print(text)

text2= 3*"Hallo Welt"
print(text2)

text3= 3*"Hallo "+"Welt"
print(text3)

print("---------------------------")

text4= "Py" "thon"
print(text4)

print("---------------------------")

print("Dieses Projekt heißt: "
"Sample.py")

print("Dieses Projekt heißt: " "Sample.py")

print("---------------------------")

word= "Python"
#      012345
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
print("")
#new word
print(word[0], end="")
print(word[1], end="")
print(word[2], end="")
print(word[3], end="")
print(word[4], end="")
print(word[5])
print("")

print("---------------------------")

word="Python"
#     012345
print(word[-0])
print(word[-5])
print(word[-4])
print(word[-3])
print(word[-2])
print(word[-1])
print("")

print(word[1:3])
#character 1 wont be counted
print("---------------------------")

word2="nohtyP"
#      012345
print(word2[-1])
print(word2[-2])
print(word2[-3])
print(word2[-4])
print(word2[-5])
print(word2[-0])
print("")

print("---------------------------")

word3="Pythonn"
#     01234567
print(word3[0:6])
print(word3[:6])
print(word3[-7:-1])
print(word3[0:7])

print("---------------------------")

word4= "HelloWelcome"
print(len(word4))

print("---------------------------")



listelement1=10
listelement2=10.10
listelement3=True
numberlist=[listelement1, listelement2, listelement3]
print(numberlist)

print(numberlist[0])
print(numberlist[1])
print(numberlist[2])
print(numberlist[-1])
print(numberlist[-2])
print(numberlist[-3])

numberlist[2]=123
print(numberlist)
numberlist.append(456)
print(numberlist)

print("---------------------------")