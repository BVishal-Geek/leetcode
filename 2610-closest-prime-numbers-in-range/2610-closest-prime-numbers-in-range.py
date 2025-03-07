class Solution:

    def sieve(self, n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:  
                for j in range(i * i, n + 1, i):  
                    is_prime[j] = False
                    
        return is_prime

    def closestPrimes(self, left: int, right: int) -> List[int]:
        stack = []

        is_prime = self.sieve(right)
        stack = [i for i in range(left, right + 1) if is_prime[i]]  # Get all primes in range

        if len(stack) < 2:
            return [-1,-1]

        diff = float("inf")
        min_index = -1
        for i in range(len(stack)-1):
            current_diff = stack[i+1] - stack[i]
            if current_diff < diff:
                diff = current_diff
                min_index = i

        return [stack[min_index], stack[min_index+1]] if min_index != -1 else [-1, -1]  
        