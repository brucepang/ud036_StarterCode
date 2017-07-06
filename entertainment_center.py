import media
import fresh_tomatoes
# construct six movie objects
titanic = media.Movie("Titanic",
	"The World's Most Beloved and Acclaimed Film",
	"https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
	"https://www.youtube.com/watch?v=2e-eXJ6HgkQ")
harry_potter_azkaban= media.Movie("Harry Potter", 
	"The Grown-up Wizard Meets His Godfather",
	"https://vignette3.wikia.nocookie.net/harrypotter/images/9/99/Harry-Potter-and-the-Prisoner-of-Azkaban-movie-poster.jpg/revision/latest?cb=20141215162758",
	"https://www.youtube.com/watch?v=lAxgztbYDbs")
gone_with_the_wind=media.Movie("Gone with the Wind",
	"Recalling Civil War and Plantation Days of South",
	"https://upload.wikimedia.org/wikipedia/en/b/b3/Gone_With_The_Wind_1967_re-release.jpg",
	"https://www.youtube.com/watch?v=8mM8iNarcRc")
roman_holiday=media.Movie("Roman Holiday",
	"The Love between a Reporter and a Royal Princess",
	"https://upload.wikimedia.org/wikipedia/en/b/b7/Roman_holiday.jpg",
	"https://www.youtube.com/watch?v=9GzCG6lpFUw")
inception = media.Movie("Inception",
	"Dream on",
	"https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
	"https://www.youtube.com/watch?v=66TuSJo4dZM")
god_father = media.Movie("The Godfather","The Story of A New York Crime Family",
	"http://celebmix.com/wp-content/uploads/2017/03/celebrating-45-years-of-the-godfather-01.jpg",
	"https://www.youtube.com/watch?v=sY1S34973zA")
# the method of fresh tomatoes takes in a list of movies as its input
movies=[titanic,harry_potter_azkaban,gone_with_the_wind,roman_holiday,inception,god_father]
fresh_tomatoes.open_movies_page(movies)
