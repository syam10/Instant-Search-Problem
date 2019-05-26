from .linked_list import LinkedList
import sys
import re

class TrieNode(object):
    '''
    Basic trie node to implement Trie data structure
    '''
    def __init__(self):
        '''
        Constructor for trie node
        '''
        self.children = [None]*26
        # a reference list to store linkedlists with all the words associated with the search string
        # formed from head to node in priority order
        self.reference_name_list = [None]*26
        self.is_end_of_word = False

class Trie(object):
    '''
    A trie class to store all the strings(along with its substrings)
    '''
    def __init__(self, lookup_dict):
        '''
        Constructor for Trie class
        Args:
            lookup_dict(dict, required): dict of csv records from a file with key as line no and value as full name
                        passed to maintain priority of the order while inserting a new string to maintain order in
                        linked list
        '''
        self.root = self.get_node()
        self.lookup_dict = lookup_dict


    def get_node(self):
        '''
        Method to create a new TrieNode
        Returns:
            TrieNode object
        '''
        return TrieNode()


    def char_index(self, char):
        '''
        Method to give the index of a char with 0 for 'a' and 25 for 'z'
        Args:
            char: input character
        Returns:
````        index of character(integer)
        '''
        diff = ord(char)-ord('a')
        return diff

    def insert_string(self, word, reference_index, is_full_word):
        '''
        Method to add a string to trie
        Args:
            word: string to be added in trie
            reference_index: reference index for the look up dict
            is_full_word: boolean value to check whether word is full or a substring
        Returns:
            None
        '''
        p_crawl = self.root
        word_length = len(word)
        #Storing each character of the string in trie
        for index in range(word_length):
            ind = self.char_index(word[index])
            if not p_crawl.children[ind]:
                p_crawl.children[ind] = self.get_node()
            # creating and storing the words associated with the character in a linked list with order
            # linked list is created from the 3rd character of the string as the use case requires to find the matchings for the strings with length > 3
            if index >= 2:
                if p_crawl.reference_name_list[ind] is None:
                    p_crawl.reference_name_list[ind] = LinkedList()
                #Inserting a node in linked list
                p_crawl.reference_name_list[ind].insert_node(reference_index, self.lookup_dict, is_full_word)
            p_crawl = p_crawl.children[ind]
            # mark last node as leaf
        p_crawl.is_end_of_word = True


    def insert_search_string(self, word, reference_index):
        '''
        Method to add a string and its all descendants(forming a substring by removing its first character every time until
        substring length reaches to 3) in the trie
        Example : word "final" will add ["final", "inal", "nal"] to trie
        Args:
            word: string to be added in trie
            reference_index: reference index in the lookup dict for the full word
        Returns:
            None
        '''
        word_list = [word[i:] for i in range(0, len(word)-2)]
        if len(word_list)==0:
            return
        self.insert_string(word_list[0], reference_index, True)
        for word in word_list[1:]:
            self.insert_string(word, reference_index, False)

    def search(self, key):
        '''
        Method to search a key and return the linked list found in the node which holds the information
        abouts words associated with the string
        Args:
            key(String, required):search string prameter
        Returns:
            returns the linked list
        '''
        word_list=None
        p_crawl = self.root
        key=re.sub('[^A-Za-z]+','', key).lower()
        length = len(key)
        #returns empty linked list as key length should be >= 3
        if length<3:
            return LinkedList()
        for level in range(length):
            index = self.char_index(key[level])
            #returns empty linked list if trie obj doesn't have any matched string in it
            if not p_crawl.children[index]:
                return LinkedList()
            word_list = p_crawl.reference_name_list[index]
            p_crawl = p_crawl.children[index]
        return word_list