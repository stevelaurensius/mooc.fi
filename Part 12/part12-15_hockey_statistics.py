import json


def output(player, team, goal, assist, contribution):
    print(player.ljust(20, ' '), team, str(goal).rjust(3, ' '), '+', str(assist).rjust(2, ' '),
          '=', str(contribution).rjust(3, ' '))


def read_file(file_name):
    with open(file_name) as my_file:
        data = my_file.read()
    players = json.loads(data)
    total_data = len(players)
    print(f'read the data of {total_data} players')
    print()
    return players


def instructions():
    command_list = ['commands:', '0 quit', '1 search for player', '2 teams', '3 countries',
                    '4 players in team', '5 players from country', '6 most points', '7 most goals']
    for command in command_list:
        print(command)
    print()


def search_for_player(players):
    player_name = str(input('name: '))
    for player in players:
        if player['name'] == player_name:
            print()
            output(player['name'], player['team'], player['goals'], player['assists'],
                   (player['goals'] + player['assists']))
            print()


def teams(data):
    result = list(set([team['team'] for team in data]))
    result.sort()
    for team in result:
        print(team)
    print()


def countries(data):
    result = list(set([country['nationality'] for country in data]))
    result.sort()
    for team in result:
        print(team)
    print()


def players_in_team(input_data):
    team = input('team: ')
    data = sorted(input_data, key=lambda x: x['name'], reverse=False)
    for player in data:
        if player['team'] == team:
            output(player['name'], player['team'], player['goals'], player['assists'],
                   (player['goals'] + player['assists']))


def players_from_country(input_data):
    country = input('country: ')
    data = sorted(input_data, key=lambda x: x['assists'] + x['goals'], reverse=True)
    for player in data:
        if player['nationality'] == country:
            output(player['name'], player['team'], player['goals'], player['assists'],
                   (player['goals'] + player['assists']))
    print()


def most_points(input_data):
    how_many = int(input('how many: '))
    data = sorted(input_data, key=lambda x: x['assists'] + x['goals'], reverse=True)
    for player in data[:how_many]:
        output(player['name'], player['team'], player['goals'], player['assists'],
               (player['goals'] + player['assists']))
    print()


def most_goals(input_data):
    how_many = int(input('how many: '))
    data = sorted(input_data, key=lambda x: (-x['goals'], x['games']))
    for player in data[:how_many]:
        output(player['name'], player['team'], player['goals'], player['assists'],
               (player['goals'] + player['assists']))
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
