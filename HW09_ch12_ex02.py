def anagrams(filename):
    with open(filename,'r') as f:
        txt=f.read()
        words=txt.split()
        list1=charsets(words)
        d={}
        for charset in list1:
            listout=[]
            for word in words:
                flag=True
                for items in charset:
                    flag = flag and (items in word)
                if flag == True:
                    listout.append(word)
            d[charset]=listout
        for keys in d:
            print(d[keys])

def anagrams2(filename):
    with open(filename,'r') as f:
        txt=f.read()
        words=txt.split()
        list1=charsets(words)
        d={}
        for charset in list1:
            listout=[]
            for word in words:
                flag=True
                for items in charset:
                    flag = flag and (items in word)
                if flag == True:
                    listout.append(word)
            d[charset]=listout
        list1=[]
        for keys in d:
            list1.append(d[keys])
        list2=sorted(list1, key=len, reverse=True)
        for items in list2:
            print(items)

def charsets(words):
    list1=[]
    for word in words:
        t=()
        for n in range(len(word)):
            t+=(word[n],)
        list1.append(t)
    list2=[]
    for tuples in list1:
        list2.append(tuple(sorted(tuples)))
    list1=list(set(list2))
    return list1

def main():
    print('\nPart1: \n')
    anagrams('anagram.txt')
    print('\n\nPart2: \n')
    anagrams2('anagram.txt')

if __name__ == '__main__':
    main()
