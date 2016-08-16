languages = {'JavaScript': 'P',
             'Arabic': 'N',
             'R': 'P',
             'Python': 'P',
             'C++': 'P',
             'Koine Greek': 'N',
             'Latin': 'N',
             'Romanian': 'N',
             'English': 'N'}


def sort1(lang):
    lang1=sorted(sorted(lang),key=lang.__getitem__)
    print("1:")
    for values in lang1:
        print("\t {}".format(values))

def sort2(lang):
    lang2=sorted(sorted(lang),key=len)
    print("2:")
    for values in lang2:
        print("\t {}".format(values))

def sort3(lang):
    lan3=sorted(sorted(lang),key=last_char,reverse=True)
    print("3:")
    for values in lang3:
        print("\t {}".format(values))

sort1(languages)
sort2(languages)
sort3(languages)

