#sacesha Coffman project
#NAMED CONSTANTS
FMERCURY = 0.38
FVENUS = 0.91
FMOON = 0.165
FMARS = 0.38
FJUPITER = 2.34
FSATURN = 0.93
FURANUS = 0.92
FNEPTUNE = 1.12
FPLUTO = 0.066

#INPUT STATEMENT FOR NAME AND WEIGHT

sName = input("what is your name?")
fWeight = float(input("what is your weight?"))


#processing- what calculations do we need

fMercury_Weight = FMERCURY*fWeight
fVenus_Weight = FVENUS*fWeight
fMoon_Weight = FMOON * fWeight
fMars_Weight = FMARS * fWeight
fJupiter_Weight = FJUPITER * fWeight
fSaturn_Weight = FSATURN * fWeight
fUranus_Weight = FURANUS * fWeight
fNeptune_Weight = FNEPTUNE * fWeight
fPluto_Weight = FPLUTO * fWeight
#output- formatting to two decimals

print(f"{sName} here are your solar system weights")
print(f'{"weight on Mercury:":<25}{fMercury_Weight:<10.2f}')
print(f'{"weight on Venus:":<25}{fVenus_Weight:<10.2f}')
print(f'{"weight on Moon:":<25}{fMoon_Weight:<10.2f}')
print(f'{"weight on Mars:":<25}{fMars_Weight:<10.2f}')
print(f'{"weight on Jupiter:":<25}{fJupiter_Weight:<10.2f}')
print(f'{"weight on Saturn:":<25}{fSaturn_Weight:<10.2f}')
print(f'{"weight on Uranus:":<25}{fUranus_Weight:<10.2f}')
print(f'{"weight on Neptune:":<25}{fNeptune_Weight:<10.2f}')
print(f'{"weight on Pluto:":<25}{fPluto_Weight:<10.2f}')

#Sacesha Coffman
#planetary weights
# what i liked about this assignment was writing the code that gave specific direction
#i like how i had to tell the program how many spaces to use and what to multiply
#i learned named constants,strings, and floats, and also two decimals


