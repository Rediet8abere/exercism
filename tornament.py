"""
input: a list of strings that contains
output: a string that represents a table
"""
string_list = ["Allegoric Alaskans;Blithering Badgers;draw", "Devastating Donkeys;Courageous Californians;draw", "Devastating Donkeys;Allegoric Alaskans;draw", "Courageous Californians;Blithering Badgers;draw", "Blithering Badgers;Devastating Donkeys;draw", "Allegoric Alaskans;Courageous Californians;draw"]
# string_list = ["Allegoric Alaskans;Blithering Badgers;win", "Devastating Donkeys;Courageous Californians;draw", "Devastating Donkeys;Allegoric Alaskans;win", "Courageous Californians;Blithering Badgers;loss", "Blithering Badgers;Devastating Donkeys;loss", "Allegoric Alaskans;Courageous Californians;win"]
def tornament(string_list):
    team_dict = {}
    # "Allegoric Alaskans": {"win": 3, "loss": 0, "draw": 1}
    teams = []
    for i in range(len(string_list)):
        teams_status = string_list[i].split(';')
        if teams_status[2] == 'win':
            if teams_status[0] in team_dict:
                # team win
                if teams_status[2] in team_dict[teams_status[0]]:
                    # print("adding")
                    team_dict[teams_status[0]][teams_status[2]] += 1
                else:
                    team_dict[teams_status[0]][teams_status[2]] = 1

            else: #teams_status[0] not in team_dict
                status_dict = {}
                status_dict[teams_status[2]] = 1
                status_dict["loss"] = 0
                team_dict[teams_status[0]] = status_dict
            if "point" in team_dict[teams_status[0]]:
                team_dict[teams_status[0]]["point"] += 3
            else:
                team_dict[teams_status[0]]["point"] = 3

        elif teams_status[2] == 'loss':
            if teams_status[1] in team_dict:

                # team win
                if teams_status[2] in team_dict[teams_status[1]]:
                    team_dict[teams_status[1]]["win"] += 1
                else:
                    team_dict[teams_status[1]]["win"] = 1
            else: #teams_status[0] not in team_dict
                status_dict = {}
                status_dict["win"] = 1
                status_dict[teams_status[2]] = 0
                team_dict[teams_status[1]] = status_dict
            if "point" in team_dict[teams_status[1]]:
                team_dict[teams_status[1]]["point"] += 3
            else:
                team_dict[teams_status[1]]["point"] = 3
        elif teams_status[2] == 'draw':
            if teams_status[1] in team_dict:

                # team win
                if teams_status[2] in team_dict[teams_status[1]]:
                    team_dict[teams_status[1]][teams_status[2]] += 1
                else:
                    team_dict[teams_status[1]][teams_status[2]] = 1
            else: #teams_status[0] not in team_dict
                status_dict = {}
                status_dict["draw"] = 1
                team_dict[teams_status[1]] = status_dict
            if "point" in team_dict[teams_status[1]]:
                team_dict[teams_status[1]]["point"] += 1
            else:
                team_dict[teams_status[1]]["point"] = 1

            if teams_status[0] in team_dict:
                # team win
                if teams_status[2] in team_dict[teams_status[0]]:
                    # print("adding")
                    team_dict[teams_status[0]][teams_status[2]] += 1
                else:
                    team_dict[teams_status[0]][teams_status[2]] = 1
            else: #teams_status[0] not in team_dict
                status_dict = {}
                status_dict[teams_status[2]] = 1
                team_dict[teams_status[0]] = status_dict
            if "point" in team_dict[teams_status[0]]:
                team_dict[teams_status[0]]["point"] += 1
            else:
                team_dict[teams_status[0]]["point"] = 1

        if teams_status[0] not in teams:
            teams.append(teams_status[0])
        if teams_status[1] not in teams:
            teams.append(teams_status[1])


    # print("team_dict: ", team_dict)
    # print("teams_status: ", teams)
    # sort
    for i in range(len(teams)):
        j = i+1
        while j<len(teams):
                if team_dict[teams[i]]["point"] < team_dict[teams[j]]["point"]:
                    temp = teams[i]
                    teams[i] = teams[j]
                    teams[j] = temp
                j += 1
        if "draw" not in team_dict[teams[i]]:
            team_dict[teams[i]]["draw"] = 0
        if "loss" not in team_dict[teams[i]]:
            team_dict[teams[i]]["loss"] = 0
        if "win" not in team_dict[teams[i]]:
            team_dict[teams[i]]["win"] = 0
    # print("team_dict: ", team_dict)
        # if "win" not in
    print("teams_status: ", team_dict["Devastating Donkeys"]["win"])
    print("Team                                         | MP |  W |  D |  L |  P")
    for i in range(len(teams)):
        win = team_dict[teams[i]]["win"]
        draw = team_dict[teams[i]]["draw"]
        loss = team_dict[teams[i]]["loss"]
        point = team_dict[teams[i]]["point"]
        print(f"{teams[i]}                           | 3 |  {win} |  {draw} |  {loss} |  {point}")




tornament(string_list)


# text = ["plant", "cat", "netflix"] # a list of words
# word_count = {}
# for word in text:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print("dictionary: ", word_count)
# print('plant' in word_count)
