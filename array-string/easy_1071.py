class Solution:

    # Brute-force
    def gcdOfStrings(self, str1: str, str2: str) -> str:
      
        if str1 + str2 != str2 + str1:
            return ""

        def bruteForce(l1, l2):
            for i in range(min(l1, l2), 0, -1):
                if l1 % i == 0 and l2 % i == 0:
                    return i
            return 1

        def euclidean(l1, l2):
            while l2:
                l1, l2 = l2, l1%l2
            return l1
        
        return str2[:euclidean(len(str1), len(str2))]