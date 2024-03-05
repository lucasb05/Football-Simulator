import random

team_num = int(input("Enter the number of teams in the league: "))
t_list =[]
player_count = []
success_chance = []
for i in range(team_num):
    t_list.append("Team " +  str(i + 1))
    player_count.append(random.randint(11, 25))
    if player_count[i] == 11:
        success_chance.append(random.randint(0, 30))
    elif 11 < player_count[i] <= 19:
        success_chance.append(random.randint(30, 70))
    elif 19 < player_count[i] <= 25:
        success_chance.append(random.randint(70, 100))
final = []
for i in range(team_num):
    final.append(str(t_list[i]) + f' - ' + str(player_count[i]) + f' players with a ' + str(success_chance[i]) + f'% chance of winning')
for i in range(team_num):
    print(final[i])