class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = list(ransomNote)
        mag = list(magazine)
        checker = []

        count = 0

        while count < len(ransom):
            for letter in ransom:
                if letter in mag:
                    mag.remove(letter)
                    checker.append(letter)
                    count += 1  
                    continue  
                else:
                    count += 1

        if ransom == checker:
            return True

        else:
            return False
