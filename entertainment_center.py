import media
import fresh_tomatoes

def main():
    toy_story = media.Movie("Toy Story",
                            "A story of a boy and his toys that come to life",
                            "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                            "https://youtu.be/4KPTXpQehio")

    avatar = media.Movie("Avatar",
                         "A marine on an alien planet",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                         "https://youtu.be/cRdxXPV9GNQ")

    deadpool = media.Movie("Deadpool",
                           "Wade Wilson is a former Special Forces operative who now works as a mercenary.",
                           "http://t2.gstatic.com/images?q=tbn:ANd9GcTvrIHJfasS6poy34esN1O5hZonXaiqfEZb4WbnbAa9qJCIL8_9",
                           "https://youtu.be/gtTfd6tISfw")
    
    it_movie = media.Movie("IT",
                            "A horror movie about a monster clown taking kids.",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcTALjGaaCwNAfgH2Fa0jVpp2mEOhGRRw1v0lkRrHlUtXyKW0buX",
                            "https://youtu.be/xKJmEC5ieOk")

    star_wars_tfa = media.Movie("Star Wars: The Force Awakens",
                                "Thirty years after the defeat of the Galactic Empire, the galaxy faces a new threat from the evil Kylo Ren and the First Order. ",
                                "http://t0.gstatic.com/images?q=tbn:ANd9GcT6nGxj1D4P-9EiVSY32sb6Ql-XQrbeK5FgM37UI6QxcZwfcfVw",
                                "https://youtu.be/sGbxmsDFVnE")

    big_hero6 = media.Movie("Big Hero 6",
                            "Robotics prodigy Hiro lives in the city of San Fransokyo.",
                            "http://t2.gstatic.com/images?q=tbn:ANd9GcQzyu98HxFhB68UKqRKSrTKknXHI-gtSTAAX0CGiKBM980CFhI1",
                            "https://youtu.be/rD5OA6sQ97M")

    movies = [toy_story, avatar, deadpool, it_movie, star_wars_tfa, big_hero6]
    
    #fresh_tomatoes.open_movies_page(movies)
    print(media.Movie.__module__)
    print(media.Movie.__name__)
    print(media.Movie.__doc__)
main()
