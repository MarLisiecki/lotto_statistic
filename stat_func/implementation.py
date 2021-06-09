from collections import Counter

import requests

from stat_func.const import LOTTO_URL_FILE
from stat_func.data_manipulation import DataManipulation
from stat_func.interfaces import AbstractInterfaceGames, AbstractInterfaceDownloadFile


class Lotto(AbstractInterfaceGames, AbstractInterfaceDownloadFile):
    def __init__(self):
        self.url_for_file = LOTTO_URL_FILE

    def most_common(self):
        list_for_analysis = self.get_merged_list()
        most_common_num = {item: item_count for item, item_count in Counter(list_for_analysis).most_common(6)}
        return most_common_num

    def check_my_numbers(self, my_list):
        check_list = DataManipulation.all_data_to_list('lotto_data.csv')
        if my_list in check_list:
            return True
        return False

    def download_file(self):
        link_to_file = self.url_for_file
        response = requests.get(link_to_file)
        with open('../lotto_data.xls', 'wb') as file:
            file.write(response.content)

    def convert_file(self):
        DataManipulation.xls_to_csv('lotto_data.xls')

    def get_merged_list(self):
        list_of_numbers = DataManipulation.merge_list(DataManipulation.all_data_to_list('lotto_data.csv'))
        return list_of_numbers


if __name__ == '__main__':
    lotto = Lotto()
    # lotto.download_file()
    lotto.convert_file()
    print(lotto.most_common().keys())
    print(lotto.check_my_numbers([6, 17, 21, 24, 27, 34]))
