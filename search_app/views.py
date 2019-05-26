from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
from .forms import SearchStringForm
from .code.main import store_csv_data_in_trie_obj, get_search_string_results

#Trie datastructure to store the csv words and look up dictionary for the reference of indes to full name
trie_obj, lookup_dict = store_csv_data_in_trie_obj()

# Create your views here.
def hello_user(request):
    '''
    view for the home page to submit a query string to search in trie obj
    '''
    return render(request, 'home_page.html', {})

def results(request):
    '''
    View to return the results found after querying the string with trie object
    '''
    search_string = request.GET.get('search_string')
    word_list, rank = get_search_string_results(search_string, trie_obj, lookup_dict)
    return render(request, 'results.html', {'results': zip(word_list, rank)})

def get_names(request):
    '''
    View to execute the serch string query on trie object and returns the result to other query
    '''
    #if this is a POST request we need to process the form data
    if request.method == 'POST':
        #create a form instance and populate it with data from the request:
        form = SearchStringForm(request.POST)
        #check whether it's valid:
        if form.is_valid():
            #redirecting to different view
            base_url = reverse('results')
            query_string = urlencode({'search_string': form.cleaned_data['search_string']})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)

    #if a GET (or any other method) we'll create a blank form
    else:
        form = SearchStringForm()
    return render(request, 'errors.html', {'form': form})