import webbrowser
"""
This module contains Movie class.
"""


class Movie():
    """
    Movie class that contains construtor and show_trailer method
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        constructor that takes in movie's title, storyline, poster,
        and trailer from youtube.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        method that call the webbrowser module to open
        the youtube website of trailer
        """
        webbrowser.open(self.trailer_youtube_url)
