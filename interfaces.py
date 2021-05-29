from abc import ABCMeta, abstractmethod


class AbstractInterfaceGames(metaclass=ABCMeta):

    @abstractmethod
    def most_common(self):
        """Find the most common numbers from the past"""

    @abstractmethod
    def check_my_numbers(self):
        """Check if the numbers have been in the past"""


class AbstractInterfaceDownloadFile(metaclass=ABCMeta):

    @abstractmethod
    def download_file(self, url):
        """Download file for selected game"""


if __name__ == '__main__':
    pass
