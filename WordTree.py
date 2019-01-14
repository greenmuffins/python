import time

class WordTree(object):
    def __init__(self, letter, children=set(), isWord = False):
        self.letter = letter
        self.children = children
        self.isWord = isWord

    def __str__(self):
        if not bool(self.children):
            return self.letter
        string = ""
        for child in self.children:
            string = string + str(self.letter) + str(child) + ','
        return string

    def add_child(self,letter):
        child = self.child_has_letter(letter)
        if bool(child):
            return child
        else:
            child = WordTree(letter,set())
            self.children.add(child)
            return child

    def child_has_letter(self,input_letter):
        #for each child check if it has the letter
        for child in self.children:
            if input_letter == child.letter:
                return child
        return None

    def has_word(self,string):
        # if the first letter doesnt match then we definitely wrong
        if string[0] != self.letter:
            return False

        #recursive case = string is 1 letter. check if we have it or not reutnr flase if we dont
        if len(string) == 1:
            if self.letter == string and self.isWord:
                return True
            else:
                return False

        #for each case return has_word(child,string-1)
        child_with_word = self.child_has_letter(string[1])

        if child_with_word is None:
            return False
        else:
            return_value = child_with_word.has_word(string[1:])
            return return_value

    def has_prefix(self,string):
        #same as has_word except doesnt check the isWord boolean
        # if the first letter doesnt match then we definitely wrong
        if string[0] != self.letter:
            return False

        #recursive case = string is 1 letter. check if we have it or not reutnr flase if we dont
        if len(string) == 1:
            if self.letter == string:
                return True
            else:
                return False

        #for each case return has_word(child,string-1)
        child_with_word = self.child_has_letter(string[1])

        if child_with_word is None:
            return False
        else:
            return_value = child_with_word.has_word(string[1:])
            return return_value

    def add_word(self,word):
        #if word[0] != self.word maybe check this?
        current_node = self
        for letter in word[1:]:
            current_node = current_node.add_child(letter)
        current_node.isWord = True

class WordDictionary(object):
    def __init__(self, children=
        {'a': WordTree('a'),
         'b': WordTree('b'),
         'c': WordTree('c'),
         'd': WordTree('d'),
         'e': WordTree('e'),
         'f': WordTree('f'),
         'g': WordTree('g'),
         'h': WordTree('h'),
         'i': WordTree('i'),
         'j': WordTree('j'),
         'k': WordTree('k'),
         'l': WordTree('l'),
         'm': WordTree('m'),
         'n': WordTree('n'),
         'o': WordTree('o'),
         'p': WordTree('p'),
         'q': WordTree('q'),
         'r': WordTree('r'),
         's': WordTree('s'),
         't': WordTree('t'),
         'u': WordTree('u'),
         'v': WordTree('v'),
         'w': WordTree('w'),
         'x': WordTree('x'),
         'y': WordTree('y'),
         'z': WordTree('z')
        }):
        self.children = children

    def add_word(self,word):
        if word[0].isalpha():
            self.children[word[0]].add_word(word)

    def has_word(self,word):
        return self.children[word[0]].has_word(word)
    # def __str__(self):
    #     string = ''
    #     for child in self.children:
    #         print(child)

    def has_prefix(self,word):
        return self.children[word[0]].has_prefix(word)

if __name__ == "__main__":

    start = time.time()

    dictionary_file = open("english.txt", "r")
    dictionary = WordDictionary()
    for word in dictionary_file:
        if (len(word.strip())) >= 3:
            dictionary.add_word(word.strip().lower())

    end = time.time()
    print(end - start)

    start = time.time()
    print (dictionary.has_word('apple'))
    end = time.time()
    print(end - start)
    start = time.time()
    print (dictionary.has_prefix('app'))
    end = time.time()
    print(end - start)

    start = time.time()
    dictionary_file = open("english.txt", "r")
    dictionary = []
    for word in dictionary_file:
        if (len(word.strip())) >= 3:
            dictionary.append(word.strip().lower())

    end = time.time()
    print(end - start)

    start = time.time()
    print('apple' in dictionary)
    end = time.time()
    print(end - start)
    start = time.time()
    for word in dictionary:
        if word.startswith('app'):
            print(True)
            break
    end = time.time()
    print(end - start)



    # dictionary = WordDictionary()
    # print(dictionary.children['a'])
    # dictionary.add_word('kevin')
    # print(dictionary.children['k'])
    # print(dictionary.has_word('kevin'))


    #     kevin = WordTree('K')
    # # print (kevin)

    # kevin.add_child('E')
    # # print(kevin)

    # kevin.add_child('V')
    # # print(kevin)

    # # print(kevin.child_has_letter('K'))
    # # print(kevin.child_has_letter('E'))
    # # print(kevin.child_has_letter('V'))

    # # print(kevin.has_word('K'))
    # # print(kevin.has_word('E'))
    # # print(kevin.has_word('V'))
    # # print(kevin.has_word('KE'))
    # # print(kevin.has_word('KV'))
    # # print(kevin.has_word('KVE'))
    # # ngo = kevin.find_child('V')

    # kevin.add_word('KAV')
    # print(kevin)

    # print(bool(kevin.child_has_letter('E')))
    # print(len(kevin.children))