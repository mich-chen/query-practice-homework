# 1. Find the user with email cats@gmail.com.
>>> user = User.query.filter_by(email='cats@gmail.com').one()
# or
>>> user = db.session.query(User).filter(User.email == 'cats@gmail.com').one()

# 2. Find any movies with the exact title “Cape Fear”.
>>> movies = Movie.query.filter_by(title='Cape Fear').all()
>>> movies = db.session.query(Movie).filter(Movie.title == 'Cape Fear').all()

# 3.Find all users with the zipcode 90703.
>>> users = User.query.filter_by(zipcode='90703').all()
>>> users = db.session.query(User).filter(User.zipcode == '90703').all()

# 4. Find all ratings of with the score of 5.
>>> ratings_of_five = Rating.query.filter_by(score=5).all()
>>> ratings_of_five = db.session.query(Rating).filter(Rating.score == 5).all()

# 5. Find the rating for the movie whose id is 7, from the user whose id is 6.
>>> rating = Rating.query.filter_by(movie_id=7, user_id=6).one()
# because rating has foreign key to Movie and User, then can access their fields
>>> rating = db.session.query(Rating).filter(Rating.movie_id == 7, Rating.user_id == 6).one()

# 6. Find all ratings that are larger than 3.
>>> ratings_larger_three = Rating.query.filter(Rating.score > 3).all()
>>> ratings_larger_three = db.session.query(Rating).filter(Rating.score > 3).all()