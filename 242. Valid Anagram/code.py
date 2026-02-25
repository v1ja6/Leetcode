class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        final_word = []
        s_list = []
        remover = []

        for letter in s:
            s_list.append(letter)
            remover.append(letter)

        for letter in t:
            if letter in remover:
                final_word.append(letter)
                remover.remove(letter)
            else:
                return False
                break
        
        if len(s_list) > len(final_word):
            return False
        
        else:
            return True
