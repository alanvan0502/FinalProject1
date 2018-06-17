#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:15:53 2018

@author: alanvan
"""

import media
import fresh_tomatoes

# Add your own movie here

toyStory = media.Movie("Toy Story", "./toystory.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "./avatar.jpeg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

deadpool = media.Movie("Deadpool", "./deadpool.jpg",
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk")

goblin = media.Movie("Goblin", "./goblin.jpg",
                     "https://www.youtube.com/watch?v=6tOxnroOTWU")

inception = media.Movie("Inception", "./inception.jpeg",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

terminator = media.Movie("Terminator", "./terminator.jpeg",
                         "https://www.youtube.com/watch?v=7SHma_9ZKfc")

# Create a list of movies

movies = [toyStory, avatar, deadpool, goblin, inception, terminator]

# Call the open_movies_page function on movies list to create the website

fresh_tomatoes.open_movies_page(movies)
