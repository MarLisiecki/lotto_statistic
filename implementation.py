from const import LOTTO_URL_FILE
from interfaces import AbstractInterfaceGames, AbstractInterfaceDownloadFile


class Lotto(AbstractInterfaceGames, AbstractInterfaceDownloadFile):
    def __init__(self):
        url_for_file = LOTTO_URL_FILE

    def most_common(self):
        pass

    def check_my_numbers(self):
        pass

    def download_file(self):
        pass


if __name__ == '__main__':
    pass
