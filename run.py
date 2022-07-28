from project.config import config
from project.helpers.decorators import access_user
from project.server import create_app

app = create_app(config)

if __name__ == '__main__':
    app.run()


# @app.shell_context_processor
# def shell():
#     return {
#         "db": db,
#         "Genre": Genre,
#     }
