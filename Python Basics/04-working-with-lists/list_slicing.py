players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[2:]) # if you dont specify the last limit, it will go till the end
print(players[:4]) # if you dont specify the first limit, it will start from the start 

# Looping through the slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())   
    
    
# copying list

players_2 = players[:]

print(players_2)