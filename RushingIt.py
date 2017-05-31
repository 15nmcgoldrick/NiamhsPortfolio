#Rushing It! tourism software developed by team Alpha 1 in St. Joseph's Secondary School Rush to inform people of events, attractions and points/areas of intrest and areas of natural beauty in the local Rush area and local North County Dublin/ Fingal region
#Developed by Daniel O'Brien, Niamh McGoldrick, Dara Cullen and Aine McCann
#Developed with Github. Python 3.7, Pythonista 3, MIT Android Studio, Google Sites and Trinket.io

from time import sleep

def history():  #This is a function, it allows you to use a set of code anywhere in your program
   print("Rush is a historical town in North County Dublin is a seaside town with a vey important historic industry in agriculture and horticulture")
   print("The fertile soils in the surrounding fields of Rush and a very mild and dry microclimate create perfect conditions for growing")
   print("Rush is more important now as a commuter town and it has a growing population as it is nearby to Dublin City (Greater Dublin Region)")

print("Welcome to our code!")
print("This code should help you find some things to do in Rush!")
print("If you are hanging out with your friends and find that you have nothing to do, this code will help you!")
print("We as teenagers know that we can get bored easily, so we want to help!")
print("An often complaint used by people our ages is THERE'S NOTHING TO DO IN RUSH! Well, here are some things to do!!")
print("We also know you want to find out intresting and exciting new things so it is important to know the facts and history of your local area")
print("Type what you would like to do from the list below.")
 #This is just an introduction to our code
answer=input("explore, relax, food, friends, learn, play, enjoy, culture")
if answer == "explore":
   print("you could walk from the Harbour on the North Beach to the Martello Tower.") #give you some options
  
elif answer == "relax":
   print("you should go for a relaxing meal in the Harbour Bar") #if you want to relax
   
elif answer == "food":
   print("The town of Rush has lots of places to get food, I would recommend the Ocean Inn. They have really nice spice bags") #the best food in rush
         
elif answer == "friends":
   print("Maybe get a speaker and a bunch of your friends and just chill out at the harbour or go to the beach!")
  
elif answer == "learn":
   print("you can go to the information boards in Kenure Park on the Kenure Demense, visit Whitestown Cemetry or vidit Baldongan Castle and enjoy the scenic view!") #enjoy the view as well as learn about the area
   history()
   
elif answer == "play":
   print("There are large GAA Playing Fields located near the town where there is frequent matches, a local running group meet-up weekly in Kenure Park and Harbour Park, there is also a soccer club, cricket club, badminton, basketball and a sailing club plus a lovely links Golf Club")
   
elif answer == "enjoy":
   print("Entertain yourself in the Millbank Theatre for frequent plays or the Rush Community Center for other interesting events")

elif answer == "culture":
   print("the rush harbour festival and the St. Patricks Day parade is a big colourfule celebration of irish culture")
   
else:
   print("this feature does not yet exist. If you have suggestions for a new feature you can contact us at @dobrienstj, @15nmcgoldrick, @15amccann and @daragdb1 on github")
sleep(3)
print("Thank you for using our new service to discover interesting places around the town of Rush!!")#closing line of code
sleep(2)
print("Please remember to check out the website: rushdublin.com")#for more information
sleep(2)
print("Also, here is a list of all the transport options from Rush Co. Dublin")#transport options
         
travel = ["33", "33a", "33x", "Northen Commuter towards Dundalk", "Northen Commuter towards Dublin City", "Fingal Express: UCD-Skerries"] #bus routes
for vehicle in travel:     
   print(vehicle)

#THE END
#thanks for reading our code 
