from googlesearch import search

query = input("enter your search here: ")

for i in search(query, num=10, stop=10, pause=3):
    print(i)

# for i in search(query, tld='com', num=10, stop=10, pause=3):
#     print(i)

# tld : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain. lang : lang stands for language.