import json, re
from Quote import *
from binary_search import *

def make_quote_json(filename, len_unique_quotes):
    quotes_author_pairs = []
    for stuff in range(len_unique_quotes):
        dic = {}
        dic["quote"] = unique_quotes[stuff].quote
        dic["author"] = unique_quotes[stuff].author
        quotes_author_pairs.append(dic)
        if (stuff + 1) % 20 == 0:   #make new json file every 20 quotes
            filename += 1
            json_maker(filename, quotes_author_pairs)
            quotes_author_pairs = []

    filename += 1
    json_maker(filename, quotes_author_pairs)

def json_maker(filename, quotes_authors):
    data = {}
    data["data"] = quotes_authors
    with open(str(filename) + '.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


quote_file = open("quote_list.txt", encoding='utf-8')
quote_list = []
for stuff in quote_file:
    quote_list.append(stuff.strip("\n"))

authors_list = []
rhsQuotationRegex = re.compile(r'’')
lhsQuotationRegex = re.compile(r'‘')
authorRegex = re.compile(r'\.? [—–―]\s?(.*)?')

for stuff in range(len(quote_list)):
    author = authorRegex.findall(quote_list[stuff]) #returns a list
    if len(author) == 0:
        authors_list.append(None)
    else:
        done_author = authorRegex.sub("", author[0])
        authors_list.append(done_author)

    #Replace author with space, so you can just get the quote by itself and account for apostrophes
    quote_list[stuff] = authorRegex.sub("", quote_list[stuff])
    quote_list[stuff] = rhsQuotationRegex.sub("\u2019", quote_list[stuff])
    quote_list[stuff] = lhsQuotationRegex.sub("\u2018", quote_list[stuff])
    quote_list[stuff] = quote_list[stuff] + "."

quote_list_class = []
unique_quotes = []
for n in range(len(quote_list)):
    quote_list_class.append(Quote(quote_list[n], authors_list[n]))

their_list = []
#load up the json file
json_quotes = json.load(open('unique_quotes.json'))


for n in range(len(json_quotes['data'])):
    their_list.append(json_quotes['data'][n]['quote'])

their_list = sorted(their_list)
for q in range(len(quote_list_class)):
    if bin_search(their_list, quote_list_class[q].quote) == -1:
        unique_quotes.append(quote_list_class[q])

make_quote_json(161, len(unique_quotes))



