class Solution:
    def strToInt(self, str: str) -> int:
        if not str:
            return 0
        start, flag = 0, 1
        int_max, int_min = 2**31 - 1, -2**31
        ans = 0

        # 去空格
        while str[start] == " ":
            start += 1
            if start == len(str):
                return 0
        
        # 判断是否正负号
        if str[start] == "-":
            flag = -1
            start += 1
        elif str[start] == "+":
            start += 1

        for char in str[start:]:
            if not "0" <= char <= "9":
                break
            if ans > int_max // 10 or (ans == int_max // 10 and ord(char) - 48 > (2**31 - (flag**2 + flag) // 2) % 10):
                return int_max if flag == 1 else int_min
            ans  = 10 * ans + (ord(char) - 48)
        return flag * ans
