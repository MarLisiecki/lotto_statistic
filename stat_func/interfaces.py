from abc import ABCMeta, abstractmethod


class AbstractInterfaceGames(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        """Initial values"""
    @abstractmethod
    def get_merged_list(self):
        """Get list of all numbers for analysis"""
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

    @abstractmethod
    def convert_file(self):
        """Convert file from xls to csv"""


if __name__ == '__main__':
    pass
