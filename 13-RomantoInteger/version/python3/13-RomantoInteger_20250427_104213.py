# Last updated: 4/27/2025, 10:42:13 AM
class Solution:
    def romanToInt(self, s: str) -> int:
        convert_map = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        res = 0

        remain = s

        while remain:
            if len(remain) > 1 and remain[:2] in convert_map:
                res += convert_map[remain[:2]]
                remain = remain[2:]
            else:
                next_char = remain[0]
                remain = remain[1:]
                res += convert_map[next_char]
        return res


