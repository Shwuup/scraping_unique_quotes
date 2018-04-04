import json, re

def make_quote_json(filename, len_unique_quotes):
    quotes_author_pairs = []
    for stuff in range(len_unique_quotes):
        dic = {}
        dic["quote"] = unique_quotes[stuff][0] + "."
        dic["author"] = unique_quotes[stuff][1]
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

#load up the json file
json_quotes = json.load(open('unique_quotes.json'))

#iterate through quote list, and compare to every other unique quote in json file
unique_quotes = []
for our_quotes in range(len(quote_list)):
    quoteRegex = re.compile(quote_list[our_quotes])
    found = False
    for their_quotes in json_quotes['data']:
        match = quoteRegex.search(their_quotes["quote"])
        if match is not None:
            found = True
            break
    if found is False:
        unique_quotes.append((quote_list[our_quotes], authors_list[our_quotes])) #tuple with unique quote and author's name

make_quote_json(157, len(unique_quotes))


