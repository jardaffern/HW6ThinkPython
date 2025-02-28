#Rather than counting numbers and sorting them after I decide to sort them as they came in to keep algorthimic complexity down
#I realized this was not very practical after starting, but it was good practice
#I believe my strategy keeps the algorithm complexity as O(n)
#But since n is the number of characters that could be in the file, the quick sort complexity of O(nLogn) will never actually cause problems.
#With my strategy runtime may be increased because of the number of computations multplied per character in string done while analyzing the file
#Two different maps
#  1: for tracking how many of a character has been read, 
#  2: maintaing a set of each character at each rank so we don't have to sort again later

def most_frequent(input):
    #initializations
    countMap = {}
    rankMap = {}
    highest = 0

    #analysis
    for i in input:
        #known character
        if i in countMap:
            count = countMap[i]
            rankMap[count].remove(i)
            count = count+1
            countMap[i] = count
            if not count in rankMap:
                rankMap[count]=set()
                highest = count
            rankMap[count].add(i)
        #new character
        else:
            if highest==0: 
                rankMap[1] = set()
                highest = 1
            countMap[i] = 1
            rankMap[1].add(i)
    
    #printing results
    print("Count : Characters")
    for j in range(highest):
        count=highest-j
        charSet = rankMap[count]
        if len(charSet) > 0:
            print(str(count) + ": ", end="")
            for char in charSet:
                print(char + " ", end="")
            print("")


#fin = open('words.txt')
#most_frequent(fin)

#testing with Lorem Ipsum
loremIpsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
most_frequent(loremIpsum)