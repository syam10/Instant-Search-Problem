class Node(object):
    '''
    Basic node class to implement a linkedlist
    '''
    def __init__(self, index_of_name, size=0, start_prefix=False):
        '''
        Constructor for the node
        Args:
            index_of_name(integer, required): index of the name stored in a lookup dict
            size(integer): size of the name in the lookup dict used for ranking according to conditions
            start_prefix(boolean): a flag variable to inform whether the starting charater for the
                traversal is actually a prefix for a name or not
        '''

        self.index_of_name = index_of_name
        self.size = size
        self.start_prefix = start_prefix
        self.next_node = None


class LinkedList(object):
    '''
    A Linkedlist class to store the info of associated names with the strings in trie
    Highest priority goes in the descending order from root node to tail node
    '''
    def __init__(self):
        '''
        Constructor while creating a linked list
        '''
        self.head = None

    def insert_node(self, index_of_name, lookup_dict, is_full_word):
        '''
        Method to insert a node in linkedlist in priority order
        Args:
            index_of_name: index of the name from the lookup dict
            lookup_dict: reference lookup dict where names are stored
            is_full_word: boolean value to check whether word is full or a substring
        Returns:
            None
        '''
        prev_node = self.head
        cur_node = self.head
        node = Node(index_of_name, len(lookup_dict[str(index_of_name)]), is_full_word)
        #inserting first element in linked list
        if cur_node is None:
            self.head = node
            return
        #insert node in the linked list in priority order with the given conditions
        while(cur_node != None):
            if (is_full_word and cur_node.start_prefix and node.size<=cur_node.size):
                if(cur_node==self.head):
                    node.next_node = cur_node
                    self.head = node
                else:
                    prev_node.next_node = node
                    node.next_node = cur_node
                break
            elif (not is_full_word and not cur_node.start_prefix and node.size <= cur_node.size):
                if (cur_node == self.head):
                    node.next_node = cur_node
                    self.head = node
                else:
                    prev_node.next_node = node
                    node.next_node = cur_node
                break
            elif (is_full_word and not cur_node.start_prefix):
                if (cur_node == self.head):
                    node.next_node = cur_node
                    self.head = node
                else:
                    prev_node.next_node = node
                    node.next_node = cur_node
                break
            else:
                prev_node = cur_node
                cur_node = cur_node.next_node

    def word_indexes_with_rank(self):
        '''
        Method to return out the words indexes along with its ranks in linked list
        Returns:
           results: list of unique words in the linked list
           rank: list of ranks for above found words in priority order
        '''
        p_crawl = self.head
        p_crawl_prev = None
        results = []
        rank = []
        while(p_crawl != None):
            #Removing duplicte names found in linked list
            #duplicates occurs with names like "Terrie Zoombeat Terbrug" and with query string "ter" as query string occurs more than once
            if p_crawl.index_of_name not in results:
                results.append(p_crawl.index_of_name)
                if p_crawl_prev is None:
                    rank.append(1)
                elif p_crawl_prev.size == p_crawl.size and p_crawl_prev.start_prefix == p_crawl.start_prefix:
                    rank.append(rank[-1])
                else:
                    rank.append(rank[-1]+1)
            p_crawl_prev = p_crawl
            p_crawl = p_crawl.next_node
        return (results, rank)