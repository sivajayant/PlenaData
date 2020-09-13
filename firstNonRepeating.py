import collections,heapq

def getFirstNonRepeating(string):
    loweredString = string.lower()
    counts = collections.Counter(loweredString)
    for char in string:
        if counts[char.lower()] == 1:
            return char,counts
    
def getOrdered(counts, string):
    queue = []
    result = []
    for i,char in enumerate(string):
        count = counts[char.lower()]
        heapq.heappush(queue, (count,i,char))
    while queue:
        result.append(heapq.heappop(queue)[2])
    return "".join(result)

print("Please enter a valid string : ")
string  = input()
char,counts = getFirstNonRepeating(string)
print("First letter that is not repeated is : "+char)
print("String in order of number of occurrences and order from the inputted string is :"+str(getOrdered(counts,string)))
