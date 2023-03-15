#!/usr/bin/env python3
"""https://leetcode.com/problems/fizz-buzz/"""


class Solution1:
    """Works but slow."""
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
                continue

            if i % 3 == 0:
                result.append('Fizz')
                continue

            if i % 5 == 0:
                result.append('Buzz')
                continue

            result.append(str(i))

        return result


class Solution2:
    """Very standard solution. Faster than Solution1."""
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result



class Solution3:
    """Doesn't work, but some interesting ideas here."""
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        for i in range(1, n + 1):
            fizz = 'Fizz' if i % 3 == 0 else ''
            buzz = 'Buzz' if i % 5 == 0 else ''
            num = str(i) if not fizz or not buzz else ''
            result.append(f'{num}{fizz}{buzz}')
        return result
