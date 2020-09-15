# Author: Jacob Noethiger jln5438@psu.edu
# Collaborator: Samantha Glenn sag5863@psu.edu
# Collaborator: Heonyrong Ha hzh5274@psu.edu
# Collaborator:Kelly Wole
# Section:2
# Breakout:4

def sum_n(n):
  if(n==0):
    return n
  else:
    return sum_n(n-1)+n

def print_n(s,n):
  if(n>0):
    print(s)
    print_n(s,n-1)

sum_n(5)

def run():
  n=int(input("Enter an int: "))
  print("sum is: "+sum_n(n)+".")
  s=input("Enter a string: ")
  print_n(s,n)

if __name__=="__main__":
  run()