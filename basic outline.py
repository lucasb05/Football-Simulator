import random

team_num = int(input("Enter the number of teams in the league: "))
t_list =[]
player_count = []
success_chance = []
for i in range(team_num):
    t_list.append(str(input("What is the name of your team?: ")))
    player_count.append(int(input("How many players are on this team?: ")))
    if player_count[i] < 11:
        success_chance.append(-1)
    elif player_count[i] == 11:
        success_chance.append(random.randint(0, 30))
    elif 11 < player_count[i] <= 19:
        success_chance.append(random.randint(30, 70))
    elif 19 < player_count[i]:
        success_chance.append(random.randint(70, 100))
    elif player_count[i] > 50:
        success_chance.append(random.randint(98, 100))
final = []
for i in range(team_num):
    if success_chance[i] == -1:
        final.append(str(t_list[i]) + f' - ' + str(player_count[i]) + f' players, cannot compete without 11 players')
    else:
        final.append(str(t_list[i]) + f' - ' + str(player_count[i]) + f' players with a ' + str(success_chance[i]) + f'% chance of winning')
for i in range(team_num):
    print(final[i])
