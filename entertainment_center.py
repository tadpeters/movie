#entertainment_center
import media
import fresh_tomatoes

a_space_odyssey = media.Movie("2001 A Space Odyssey",
	"Humanity finds a mysterious, obviously artificial, object buried beneath the Lunar surface and, with the intelligent computer H.A.L. 9000, sets off on a quest.",
	"http://i174.photobucket.com/albums/w91/warpigx/2001-a-space-odyssey-movie-poster-aa0_zpsxmezpy7u.png",
	"https://www.youtube.com/watch?v=lfF0vxKZRhc")

eyes_wide_shut = media.Movie("Eyes Wide Shut",
	"A New York City doctor, who is married to an art curator, pushes himself on a harrowing and dangerous night-long odyssey of sexual and moral discovery after his wife admits that she once almost cheated on him.",
	"http://ia.media-imdb.com/images/M/MV5BMjA5NTUwNjI1N15BMl5BanBnXkFtZTYwOTE1ODc5._V1__SX942_SY760_.jpg",
	"https://www.youtube.com/watch?v=YEfyfcEdW4Y")

The_Shining = media.Movie("The Shining",
	"A family heads to an isolated hotel for the winter where an evil and spiritual presence influences the father into violence, while his psychic son sees horrific forebodings from the past and of the future.",
	"http://www.cinemasterpieces.com/82011/theshiningmay11.jpg",
	"https://www.youtube.com/watch?v=S014oGZiSdI")

The_Killing = media.Movie("The Killing",
	"Crooks plan and execute a daring race-track robbery.",
	"http://www.conventionscene.com/wp-content/uploads/2014/05/dc-eb.jpg",
	"https://www.youtube.com/watch?v=gAe1CJWH_B8")

Paths_of_Glory = media.Movie("Paths of Glory",
	"When soldiers in World War I refuse to continue with an impossible attack, their superior officers decide to make an example of them.",
	"http://www.umbertocantone.it/wp-content/uploads/2014/10/kubrick-510.jpg",
	"https://www.youtube.com/watch?v=nmDA60X-f_A")

Dr_Strangelove = media.Movie("Dr Strangelove",
	"An insane general triggers a path to nuclear holocaust that a war room full of politicians and generals frantically try to stop.",
	"http://ia.media-imdb.com/images/M/MV5BMTU2ODM2NTkxNF5BMl5BanBnXkFtZTcwOTMwMzU3Mg@@._V1_SX640_SY720_.jpg",
	"https://www.youtube.com/watch?v=IutX5AGEYZc")


def main():
  movies = [a_space_odyssey, eyes_wide_shut, The_Shining, The_Killing, Paths_of_Glory, Dr_Strangelove]
  fresh_tomatoes.open_movies_page(movies)


main()