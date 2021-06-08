import itertools

import pandas as pd


class DataManipulation:
    @staticmethod
    def xls_to_csv(file):
        read_file = pd.read_excel(file)
        read_file.to_csv('lotto_data.csv', index=None, header=True)

    @staticmethod
    def all_data_to_list(file_name):
        data = pd.read_csv(file_name)
        data.drop(data.columns[0], axis=1, inplace=True)
        data.drop(data.columns[0], axis=1, inplace=True)
        output_list = [list(x) for x in data.values]
        return output_list

    @staticmethod
    def merge_list(input_list):
        merged_list = list(itertools.chain.from_iterable(input_list))
        return merged_list
