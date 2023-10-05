from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


class Application:
    def __init__(self) -> None:
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")
        self._user_choice = None
        self.run()

    def show_menu(self):
        menu = """What Would You like to do?
        1 - List all albums
        2 - List all artists"""

        print(menu, "\n")

    def get_user_choise(self):
        while self._user_choice != "1" and self._user_choice != "2":
            self._user_choice = input("Choice 1 or 2: ")

    def run(self):
        self.show_menu()
        self.get_user_choise()
        if self._user_choice == "1":
            repo = AlbumRepository(self._connection)
        else:
            repo = ArtistRepository(self._connection)

        data = repo.all()
        for entry in data:
            print(entry)


if __name__ == "__main__":
    app = Application()
