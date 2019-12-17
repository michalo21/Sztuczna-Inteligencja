import random
# funkcje programu 
def checkA(vector):
  howmanyA = 0
  vector1,vector2 = vector.split("|")
  for line in wektory:
    
    if(vector1 == line[0] and vector2 == line[1] and line[2].strip() is "A"):
      howmanyA += 1
  
  return howmanyA

def checkB(vector):
  howmanyB = 0
  vector1,vector2 = vector.split("|")
  for line in wektory:
    if(vector1 == line[0] and vector2 == line[1] and line[2].strip() == "B"):
      howmanyB += 1
  return howmanyB

def checkC(vector):
  howmanyC = 0
  vector1,vector2 = vector.split("|")
  for line in wektory:
    if(vector1 == line[0] and vector2 == line[1] and line[2].strip() == "C"):
      howmanyC += 1
  return howmanyC


def validiator(vector):
  if(checkA(vector) > checkB(vector) and checkA(vector) > checkC(vector)):
    print("Nalezy do A")
  elif(checkA(vector) < checkB(vector) and checkB(vector) > checkC(vector)):
    print("Nalezy do B")
  elif(checkA(vector)< checkC(vector) and checkB(vector) < checkC(vector)):
    print("Nalezy do C")
  elif(checkA(vector) == checkB(vector) and checkA(vector) > checkC(vector)):
    rand = random.randint(0,1)
    if( rand == 0):
      print("Nalezy do A")
    else:
      print("Nalezy do B")
  elif(checkA(vector) == checkC(vector) and checkA(vector) > checkB(vector)):
    rand = random.randint(0,1)
    if( rand == 0):
      print("Nalezy do A")
    else:
      print("Nalezy do C")
  elif(checkB(vector) == checkC(vector) and checkB(vector) > checkA(vector)):
    rand = random.randint(0,1)
    if( rand == 0):
      print("Nalezy do B")
    else:
      print("Nalezy do C")
  elif(checkA(vector) == checkC(vector) and checkA(vector) == checkB(vector) and checkB(vector) == checkC(vector) and checkA(vector) != 0 and checkB(vector) != 0 and checkC(vector) != 0):
    rand = random.randint(0,2)
    if( rand == 0):
      print("Nalezy do A");
    elif(rand == 1):
      print("Nalezy do B");
    else:
      print("Nalezy do C");
  elif(checkA(vector) == 0 and checkB(vector) == 0 and checkC(vector) == 0):
      print("Brak potrzebnych danych");

## main programu

while(True):
  file = open("learning.txt", "r");
  wektory = []
  vector = input()
  for i, line in enumerate(file): 
    wektory.append(line.split("|")) ##dzielenie pliku na paczki odbywa sie poprzez odpowiednie wywolanie ifa z numerem wczytanej linijki z pliku. Ostatni i to 149 poniewaz plik ma n = 150 lini a i = n-1 wiec 149.
    if(i == 30):
        print("Przypisanie klasy po pierwszej paczce danych")
        validiator(vector)
    elif( i == 70 ):
        print("Przypisanie klasy po drugiej paczce danych")
        validiator(vector)
    elif( i == 100 ):
        print("Przypisanie klasy po trzeciej paczce danych")
        validiator(vector)
    elif( i == 135):
        print("Przypisanie klasy po czwartej paczce danych")
        validiator(vector)
    elif(i == 149):
        print("Przypisanie klasy po ostatniej paczce danych")
        validiator(vector)
  file.close()
  print("Sprawdz nowy zakres: ")


  




    
    
