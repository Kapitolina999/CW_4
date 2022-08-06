from project.dao.models import UsersMovies


class FavouriteMovieDAO:
    def __init__(self, session):
        self.session = session

    # Поиск фильма пользователя в UsersMovies
    def get_user_movie(self, uid, mid):
        return self.session.query(UsersMovies).filter(UsersMovies.user_id == uid, UsersMovies.movie_id == mid).one()

    # Создаем пару пользователь-фильм
    def create(self, uid, mid):
        user_movie = UsersMovies(user_id=uid, movie_id=mid)
        self.session.add(user_movie)
        self.session.commit()
        return user_movie

    def delete(self, uid, mid):
        user_movie = self.get_user_movie(uid, mid)
        self.session.delete(user_movie)
        self.session.commit()
        return user_movie
