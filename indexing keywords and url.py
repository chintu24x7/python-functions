# A procedure, add_to_index, that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already in the index, add the url
# to the list of urls associated with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index,keyword,url):
    i = 0
    for a in index:
        if a[0] == keyword:
            if url not in a[1]:
                a[1].append(url)
                return
        ++i
    index.append([keyword,[url]])
    return





#for testing:
#add_to_index(index,'udacity','http://udacity.com')
#add_to_index(index,'computing','http://acm.org')
#add_to_index(index,'udacity','http://npr.org')
#print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]


