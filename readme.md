# Instant-Search-Application
A sample Django application to search a given query term from csv file 
using data structures Trie and Linked list 

### Installing dependencies
```
pip3 install -r requirements.txt
```

### Starting Application
1. Place your csv file "data.csv" in "search_app/resources" folder  
2. Change your current directory to project root folder and start django server
```
python3 manage.py runserver 
```
3. If run locally visit localhost:8000 and enter the string to get results



###Implementation logic
1. Read data from csv file and store each string and its substring(formed by removing its first character every time until
substring length reaches to 3 (Example: word "final" will form ["final", "inal", "nal"])) in Trie data structure
2. Trie Object contains two lists in each node, where one list stores the information about child nodes and the other list stores a 
reference to a linked list mapped to each item of first list  
3. Referred Linked List contains the information about matched words from csv file with the string formed 
from trie root node to its current node in priority order
4. When a search string is queried upon trie object, it will look for the query string in trie, if present it will return
the linked list mapped to final character of the string otherwise None
5. From Linked list we will be able to retrieve the matched words with rank


