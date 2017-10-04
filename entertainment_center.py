import media
import fresh_tomatoes


def main():
    """This application creates several Movie instances then stores them in an
       array. The array is then passed to the
       fresh_tomatoes.open_movies_page(movies), so it can open a browser to
       display a movie trailer webpage."""

    toy_story = media.Movie("Toy Story",
                            "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",  # NOQA
                            "November 22, 1995",
                            "1h 21m",
                            "Woody, a good-hearted cowboy doll who belongs to "
                            "a young boy named Andy, sees his position as "
                            "Andy's favorite toy jeopardized when his parents "
                            "buy him a Buzz Lightyear action figure.",
                            "https://youtu.be/4KPTXpQehio")

    avatar = media.Movie("Avatar",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",  # NOQA
                         "December 18, 2009",
                         "2h 42m",
                         "On the lush alien world of Pandora live the Na'vi, "
                         "beings who appear primitive but are highly evolved.",
                         "https://youtu.be/cRdxXPV9GNQ")

    deadpool = media.Movie("Deadpool",
                           "http://t2.gstatic.com/images?q=tbn:ANd9GcTvrIHJfasS6poy34esN1O5hZonXaiqfEZb4WbnbAa9qJCIL8_9",  # NOQA
                           "February 12, 2016",
                           "1h 48m",
                           "Wade Wilson is a former Special Forces operative "
                           "who now works as a mercenary.",
                           "https://youtu.be/gtTfd6tISfw")

    it_movie = media.Movie("IT",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcTALjGaaCwNAfgH2Fa0jVpp2mEOhGRRw1v0lkRrHlUtXyKW0buX",  # NOQA
                            "September 8, 2017",
                            "2h 15m",
                            "Seven young outcasts in Derry, Maine, are about "
                            "to face their worst nightmare -- an ancient, "
                            "shape-shifting evil that emerges from the sewer "
                            "every 27 years to prey on the town's children.",
                            "https://youtu.be/xKJmEC5ieOk")

    star_wars_tfa = media.Movie("Star Wars: The Force Awakens",
                                "http://t0.gstatic.com/images?q=tbn:ANd9GcT6nGxj1D4P-9EiVSY32sb6Ql-XQrbeK5FgM37UI6QxcZwfcfVw",  # NOQA
                                "December 18, 2015",
                                "2h 15m",
                                "Thirty years after the defeat of the Galactic"
                                " Empire, the galaxy faces a new threat from "
                                "the evil Kylo Ren and the First Order. ",
                                "https://youtu.be/sGbxmsDFVnE")

    big_hero6 = media.Movie("Big Hero 6",
                            "http://t2.gstatic.com/images?q=tbn:ANd9GcQzyu98HxFhB68UKqRKSrTKknXHI-gtSTAAX0CGiKBM980CFhI1",  # NOQA
                            "November 7, 2014",
                            "1h 48m",
                            "Robotics prodigy Hiro lives in the city of San "
                            "Fransokyo.",
                            "https://youtu.be/rD5OA6sQ97M")

    movies = [toy_story, avatar, deadpool, it_movie, star_wars_tfa, big_hero6]

    fresh_tomatoes.open_movies_page(movies)


main()
