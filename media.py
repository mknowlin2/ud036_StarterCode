import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    # Class variables
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # This is a constructor
    def __init__(self, movie_title, movie_storyline, poster_img, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
