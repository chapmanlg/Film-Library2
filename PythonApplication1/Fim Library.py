import random
import lgc
x=True

Film_Lib = [
                ['Local Hero', 'Comedy'],
                ['Jaws', 'Horror'],
                ['Forest Gump', 'Drama'],
                ['Star Wars', 'SciFi'],
                ['Toy Story', 'Family']
           ]
while x is True:
    film_no = random.randint(0,4)
    ViewFilm = input("Do you want to watch the Film? " + str(Film_Lib[film_no]))
    
    if str.upper(ViewFilm) == "YES":
        print("Enjoy Watching! ")
        x = False
    else :
        print("How about this one ? ")



        