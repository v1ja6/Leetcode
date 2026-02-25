class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        list1 = []
        list2 = []

        for letter in word1:
            list1.append(letter)
        for letter in word2:
            list2.append(letter)
     
        while True:
            if len(list1) == 0 and len(list2) == 0:
                break

            else:
                looper = 1

                if looper == 1 or looper == 2:
                    while looper == 1:
                        if len(list1) == 0 and len(list2) == 0:
                            looper = 3

                        elif len(list1) == 0:
                            looper = 2
                    
                        else:
                            merged.append(list1[0])
                            list1.pop(0)
                            looper = 2

                    while looper == 2:
                        if len(list1) == 0 and len(list2) == 0:
                            looper = 3

                        elif len(list2) == 0:
                            looper = 1
                        
                        else:
                            merged.append(list2[0])
                            list2.pop(0)
                            looper = 1

                else:
                    break

        return ''.join(merged)
