class WeatherStation:
    def __init__(self, station_name: str):
        self.__station_name = station_name
        self.__observation = []

    def add_observation(self, observation: str):
        self.__observation.append(observation)

    def latest_observation(self):
        if len(self.__observation) == 0:
            return ''
        else:
            return self.__observation[-1]

    def number_of_observations(self):
        return len(self.__observation)

    def __str__(self):
        return f'{self.__station_name}, {len(self.__observation)} observations'


if __name__ == '__main__':
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)
