import csv
import math


def get_station_data(filename: str):
    result = {}
    with open(filename) as file:
        for line in csv.reader(file, delimiter=';'):
            if line[0] == 'Longitude':
                pass
            else:
                result[line[3]] = (float(line[0]), float(line[1]))
    return result


def distance(stations: dict, station1: str, station2: str):
    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]
    latitude1 = stations[station1][1]
    latitude2 = stations[station2][1]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km ** 2 + y_km ** 2)
    return distance_km


def greatest_distance(stations: dict):
    max_distance = 0
    station_pair = ("", "")

    station_names = list(stations.keys())
    num_stations = len(station_names)

    for i in range(num_stations):
        for j in range(i + 1, num_stations):
            station1 = station_names[i]
            station2 = station_names[j]
            dist = distance(stations, station1, station2)

            if dist > max_distance:
                max_distance = dist
                station_pair = (station1, station2)

    return station_pair[0], station_pair[1], max_distance


if __name__ == '__main__':
    stations = get_station_data('stations2.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
