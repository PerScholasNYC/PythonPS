#define the function and arguments
#print desired results for function

def gamer(xbox, playstation, nintendo):
    print(f"Jacob has {xbox} games for his Xbox 1")
    print(f"Billy wants to own {playstation} playstation consoles")
    print(f"Tim used to have {nintendo} swich console \n")

#print a statement
#call on function and give inoput

print("The life of a gamer")
gamer(20, 5, 6)

#asign variables to use within function
#call on function with variables
print("I can also show the results using variables")
xbone = 30
PS4 = 3
Wii = 20

gamer(xbone, PS4, Wii)

#call on function with math problem as input
print("Using math")
gamer(1 + 6, 5 + 20, 10 + 11)

#call on function using in put and varibles
print("Using a combination of math and variables")
gamer(xbone + 3, PS4 + 2, Wii + 5)
