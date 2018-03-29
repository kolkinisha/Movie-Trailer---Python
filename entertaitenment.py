import media
import fresh_tomatoes

toystory=media.Movie("TOY STORY",
                     "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                     "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                     "http://www.imdb.com/title/tt0114709/videoplayer/vi2052129305?ref_=tt_ov_vi")
#print(toystory.storyline)

avatar=media.Movie("AVATAR",
                   "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show()

iceage=media.Movie("ICE AGE",
                   "Set during the Ice Age, a sabertooth tiger, a sloth, and a wooly mammoth find a lost human infant, and they try to return him to his tribe.",
                   "https://upload.wikimedia.org/wikipedia/en/3/3c/Ice_Age_%282002_film%29_poster.jpg",
                   "https://www.youtube.com/watch?v=Ohq6NmKMja8")

jungle=media.Movie("JUNGLE BOOK",
                   "After a threat from the tiger Shere Khan forces him to flee the jungle, a man-cub named Mowgli embarks on a journey of self discovery with the help of panther, Bagheera, and free spirited bear, Baloo.",
                   "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg",
                   "https://www.youtube.com/watch?v=5mkm22yO-bs")

mad=media.Movie("MADAGASCAR",
                "Spoiled by their upbringing and unaware of what wildlife really is, four animals from the New York Central Zoo escape, unwittingly assisted by four absconding penguins, and find themselves in Madagascar.",
                "https://upload.wikimedia.org/wikipedia/en/3/36/Madagascar_Theatrical_Poster.jpg",
                "https://www.youtube.com/watch?v=fq5zU9T_Hl4")

bread=media.Movie("THE BREADWINNER",
                  "A headstrong young girl in Afghanistan disguises herself as a boy in order to provide for her family.",
                  "https://upload.wikimedia.org/wikipedia/en/7/78/The_Breadwinner_%28film%29_poster.jpg",
                  "https://www.youtube.com/watch?v=yAuX-paLc20")
movie=[toystory, avatar,iceage,jungle,mad,bread]
fresh_tomatoes.open_movies_page(movie)
