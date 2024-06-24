import json


def read_file(file_name):
    with open(file_name) as my_file:
        data = my_file.read()
    players = json.loads(data)
    total_data = len(players)
    print(f'read the data of {total_data} players')
    print()
    return players


def instructions():
    print('commands:')
    print('0 quit')
    print('1 search for player')
    print('2 teams')
    print('3 countries')
    print('4 players in team')
    print('5 players from country')
    print('6 most points')
    print('7 most goals')
    print()


def search_for_player(players):
    player_name = str(input('name: '))
    for player in players:
        if player['name'] == player_name:
            player_output = player['name']
            team_output = player['team']
            goal_output = player['goals']
            assist_output = player['assists']
            contributions = goal_output + assist_output
            print()
            print(player_output.ljust(20, ' '),
                  team_output,
                  str(goal_output).rjust(3, ' '),
                  '+',
                  str(assist_output).rjust(2, ' '),
                  '=',
                  str(contributions).rjust(3, ' '))
            print()


def teams(data):
    result = [team['team'] for team in data]
    result = list(set(result))
    result.sort()
    for team in result:
        print(team)
    print()


def countries(data):
    result = [country['nationality'] for country in data]
    result = list(set(result))
    result.sort()
    for team in result:
        print(team)
    print()


def players_in_team(input_data):
    team = input('team: ')
    data = sorted(input_data, key=lambda x: x['name'], reverse=False)
    for player in data:
        if player['team'] == team:
            player_output = player['name']
            team_output = player['team']
            goal_output = player['goals']
            assist_output = player['assists']
            contributions = goal_output + assist_output
            print(player_output.ljust(20, ' '),
                  team_output,
                  str(goal_output).rjust(3, ' '),
                  '+',
                  str(assist_output).rjust(2, ' '),
                  '=',
                  str(contributions).rjust(3, ' '))
    print()


def players_from_country(input_data):
    country = input('country: ')
    data = sorted(input_data, key=lambda x: x['assists'] + x['goals'], reverse=True)
    for player in data:
        if player['nationality'] == country:
            player_output = player['name']
            team_output = player['team']
            goal_output = player['goals']
            assist_output = player['assists']
            contributions = goal_output + assist_output
            print(player_output.ljust(20, ' '),
                  team_output,
                  str(goal_output).rjust(3, ' '),
                  '+',
                  str(assist_output).rjust(2, ' '),
                  '=',
                  str(contributions).rjust(3, ' '))
    print()


def most_points(input_data):
    how_many = int(input('how many: '))
    data = sorted(input_data, key=lambda x: x['assists'] + x['goals'], reverse=True)
    for player in data[:how_many]:
        player_output = player['name']
        team_output = player['team']
        goal_output = player['goals']
        assist_output = player['assists']
        contributions = goal_output + assist_output
        print(player_output.ljust(20, ' '),
              team_output,
              str(goal_output).rjust(3, ' '),
              '+',
              str(assist_output).rjust(2, ' '),
              '=',
              str(contributions).rjust(3, ' '))
    print()


def most_goals(input_data):
    how_many = int(input('how many: '))
    data = sorted(input_data, key=lambda x: (-x['goals'], x['games']))
    for player in data[:how_many]:
        player_output = player['name']
        team_output = player['team']
        goal_output = player['goals']
        assist_output = player['assists']
        contributions = goal_output + assist_output
        print(player_output.ljust(20, ' '),
              team_output,
              str(goal_output).rjust(3, ' '),
              '+',
              str(assist_output).rjust(2, ' '),
              '=',
              str(contributions).rjust(3, ' '))
    print()


def execute():
    file_name = input('file name: ')
    players = read_file(file_name)
    instructions()
    while True:
        user_command = int(input('commands: '))
        if user_command == 0:
            break
        elif user_command == 1:
            search_for_player(players)
        elif user_command == 2:
            teams(players)
        elif user_command == 3:
            countries(players)
        elif user_command == 4:
            players_in_team(players)
        elif user_command == 5:
            players_from_country(players)
        elif user_command == 6:
            most_points(players)
        elif user_command == 7:
            most_goals(players)


execute()