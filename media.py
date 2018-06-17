#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:14:29 2018

@author: alanvan
"""


class Movie(object):
    """
    Class Movie with 3 parameters (title, poster_image_url,
    trailer_youtube_url)

    Attributes
    ----------
    title : str
        Title of the movie
    poster_image_url : str
        URL link for the Poster Image of movie
    trailer_youtube_url: str
        URL link for the Trailer of the movie

    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
