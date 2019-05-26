import csv
import re
import os

from datetime import datetime
from .trie import Trie

def store_csv_data_in_trie_obj():
    '''
    Method to store csv records in a Trie datastructure object.
    This Trie object will be used in the api to retrieve names from the search strings
    At present, it reads a csv file 'data.csv from resources folder

    Returns:
        trie_obj: A Trie obj with all the csv records stored in it
        lookup_dict: A python dict object with keys as line_no and values as full name(first_name+middle_name+last_name)
    '''
    app_dir =os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    file_path = os.path.join(app_dir, 'resources', 'data.csv')
    lookup_dict = dict()
    trie_obj = Trie(lookup_dict)

    #reading data from csv file
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            #removing header from saving it in trie obj
            if line_count == 0:
                line_count += 1
                continue
            #Forming a full name which is retrieved after a match with given earch string
            lookup_dict[str(line_count)] = " ".join(row)
            trie_obj.lookup_dict = lookup_dict
            word_list = lookup_dict[str(line_count)].split(" ")
            for word in word_list:
                #Removing special characters and converting it into lower case to maintain consistency
                trie_obj.insert_search_string(re.sub('[^A-Za-z]+', '', word).lower(), str(line_count))
            line_count += 1
    return (trie_obj, lookup_dict)

def get_search_string_results(string_value, trie_obj, lookup_dict):
    '''
    Method to search a matching string from Trie obj and returns the words found along with its rank
    Args:
        string_value: query string to be searched in Trie obj
        trie_obj: Trie obj in which data is stored
        lookup_dict: Look up Dictionary to find out full names

    Returns:
        words: a list of matched words with given query string
        rank: a list of corresponding ranks for the above found words
    '''
    start_time = datetime.now()
    #querying to find matched with given string, returns a linked list
    word_list = trie_obj.search(string_value)
    #Given out two lists with ranking the words list
    word_list_indexs, rank = word_list.word_indexes_with_rank()
    print("result indexes are {}".format(str(word_list_indexs)))
    words = [lookup_dict[index] for index in word_list_indexs]
    end_time = datetime.now()
    exec_time = (end_time - start_time).total_seconds()
    print("Total Execution time : {}".format(exec_time))
    return (words, rank)