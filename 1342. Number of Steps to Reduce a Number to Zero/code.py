class Solution:
    def numberOfSteps(self, num: int) -> int:
        new_number = num
        steps = 0

        while True:
            if new_number == 0:
                break
            elif (new_number % 2) == 0:
                new_number = new_number / 2
                steps += 1
                continue
            else:
                new_number -= 1
                steps += 1
                continue
        return steps

 
