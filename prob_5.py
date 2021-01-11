"""
Problem Statement:-
You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user. You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the maximum number of matching words with the query.

Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

Input:
Please input your query string

“Python is”

Output:
3 results found:

python is not python snake
python is good
Python is cool
"""
print("Enter the length of list of sentences")
n = int(input())
lst_sen = []
for i in range(n):
    print("enter the sentence in list")
    lst_sen.append(input().lower())
print(lst_sen)
search = input("Please enter your query\n").lower()
print(search)
search_lst = search.split(' ')
print(search_lst)
lst_occ = []
for i in lst_sen:
    count = 0
    for j in search_lst:
        if i.count(j)>0:
            count = count + i.count(j)
    lst_occ.append(count)
for i in range(0,len(lst_sen)):
    print(lst_sen[lst_occ.index(max(lst_occ))])
    lst_occ[lst_occ.index(max(lst_occ))] = -2