# 1. Find the user with email cats@gmail.com.
>>> user = User.query.filter_by(email='cats@gmail.com').one()
# or
>>> user = db.session.query(User).filter(User.email == 'cats@gmail.com').one()

# 2. Find any movies with the exact title “Cape Fear”.
>>> movies = Movie.query.filter_by(title='Cape Fear').all()
>>> movies = db.session.query(Movie).filter(Movie.title == 'Cape Fear').all()