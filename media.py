import webbrowser

class Media():
    """ This class provides a way to store base media related information

        Attributes:
            media_name: The name of the media object.
            media_image: A location reference of an image of the media object.
            media_release_date: The release date of the media object
            media_length: The media object's length in minutes.
    """
    def __init__(self, media_name, media_image, media_release_date, media_length):
        """Inits Media with media_name, media_image, media_release_date, and media_length."""
        print("INFO: Media Class Constructor Called")
        self.media_name = media_name
        self.media_image = media_image
        self.media_release_date = media_release_date
        self.media_length = media_length

class Movie(Media):
    """ This class provides a way to store movie related information

        Parent Class: media.Media

        Attributes:
            media_name: The name of the media object.
            media_image: A location reference of an image of the media object.
            media_release_date: The release date of the media object
            media_length: The media object's length in minutes.
            movie_storyline: A brief synopsis of the movie.
            movie_trailer_youtube: A url reference to the movie trailer on YouTube
    """
    # This is a constructor
    def __init__(self, media_name, media_image, media_release_date, media_length, movie_storyline,
                 movie_trailer_youtube):
        """Inits Movie with media_name, media_image, media_release_date,
           media_length, movie_storyline and movie_trailer_youtube."""
        print("INFO: Movie Class Constructor Called")
        Media.__init__(self, media_name, media_image, media_release_date, media_length)
        self.movie_storyline = movie_storyline
        self.movie_trailer_youtube = movie_trailer_youtube

    def show_trailer(self):
        """show_trailer opens a browser to the movie_trailer_youtube"""
        webbrowser.open(self.movie_trailer_youtube)
