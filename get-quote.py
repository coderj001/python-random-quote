import random
import sys

def randNum(num):
    return random.randint(0,num)

def randomquote():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  return quotes[randNum(len(quotes))]

def addquote(quote):
    f=open("quotes.txt","+a")
    f.write(quote+"/n")
    f.close()

def main():
    arg=sys.argv
    arg.pop(0)
    
    if arg:
        if arg[0] == '-a':
            arg.pop(0)
            addquote(arg[0])
            arg.pop(0)
    else:
        randomquote()

    if arg:
        if arg[0] == '-n':
            arg.pop(0)
            for i in range(0,int(arg[0])):
                print(randomquote(),end="")
            arg.pop(0)
            print()

if __name__== "__main__":
  main()
