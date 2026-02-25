class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for integer in range(1, n+1):
            
            if (integer % 3) == 0 and (integer % 5) == 0:
                answer.append("FizzBuzz")
