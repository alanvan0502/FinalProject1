#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:15:53 2018

@author: alanvan
"""

import media
import fresh_tomatoes

#Add your own movie here

toyStory = media.Movie("Toy Story", "https://image.tmdb.org/t/p/original/rhIRbceoE9lR4veEXuwCC2wARtG.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "https://ca.movieposter.com/posters/archive/main/98/MPW-49433", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

deadpool = media.Movie("Deadpool","https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/04eafb25626631.5634844b7293f.jpg", "https://www.youtube.com/watch?v=ONHBaC-pfsk")

goblin = media.Movie("Goblin", "https://m.media-amazon.com/images/M/MV5BZTg0YmQxZTgtMzgwYi00N2NhLTlkMWYtOWYwNDA1YjkxMmViL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMzE4MDkyNTA@._V1_SY1000_CR0,0,692,1000_AL_.jpg", "https://www.youtube.com/watch?v=6tOxnroOTWU")

inception = media.Movie("Inception", "https://ca.movieposter.com/posters/archive/main/101/MPW-50904", "https://www.youtube.com/watch?v=d3A3-zSOBT4")

terminator = media.Movie("Terminator", "https://ca.movieposter.com/posters/archive/main/12/MPW-6353", "https://www.youtube.com/watch?v=7SHma_9ZKfc")


movies = [toyStory, avatar, deadpool, goblin, inception, terminator]
fresh_tomatoes.open_movies_page(movies)