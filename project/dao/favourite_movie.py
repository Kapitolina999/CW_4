from project.dao.models import users_movies


class FavouriteMovieDAO:
    def __init__(self, session):
        self.session = session

    # Добавляем пару пользователь-фильм в таблицу
    def create(self, uid, mid):
        user_movie = users_movies.insert().values(user_id=uid, movie_id=mid)
        self.session.execute(user_movie)
        self.session.commit()
        return user_movie

    def delete(self, uid, mid):
        user_movie = users_movies.delete().where(users_movies.c.user_id == uid, users_movies.c.movie_id == mid)
        self.session.execute(user_movie)
        self.session.commit()
        return user_movie
