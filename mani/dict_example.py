import operator 

fulltext  = "hello mani how are you mani what are you doing mani"

wordlist = fulltext.split()
worddictionary = {}

for word in wordlist:
    if word in worddictionary:
        #increase
        worddictionary[word] +=1
    else:
        #add to the dictionary
        worddictionary[word] =1

sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1),reverse = True)

print(worddictionary)

print(sortedwords)