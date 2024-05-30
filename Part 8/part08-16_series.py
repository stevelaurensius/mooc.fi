class Series:
    def __init__(self, title: str, season: int, genre: list):
        self.title = title
        self.season = season
        self.genre = genre
        self.rating = []

    def rate(self, rating):
        self.rating.append(rating)

    def __str__(self):
        genre_string = ', '.join(self.genre)
        if self.rating == []:
            rating = 'no ratings'
        else:
            avg_rating = sum(self.rating) / len(self.rating)
            rating_qty = len(self.rating)
            rating = f'{rating_qty} ratings, average {avg_rating:.1f} points'
        return f'{self.title} ({self.season} seasons)\ngenres: {genre_string}\n{rating}'


def minimum_grade(rating: float, series_list: list):
    result_list = [x for x in series_list if sum(x.rating) >= rating]
    return result_list


def includes_genre(genre: str, series_list: list):
    result_list = [x for x in series_list if genre in x.genre]
    return result_list


if __name__ == '__main__':
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
