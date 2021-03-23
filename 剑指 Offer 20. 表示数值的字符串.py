class Solution:
    def isNumber(self, s: str) -> bool:
        status = [
            {"blank": 0, "sign": 1, "digit": 2, "dot": 4},
            {"digit": 2, "dot": 4},
            {"digit": 2, "dot": 3, "Ee": 5, "blank": 8},
            {"digit": 3, "Ee": 5, "blank": 8},
            {"digit": 3},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7, "blank": 8},
            {"blank": 8}
        ]

        now = 0
        for char in s:           
            if char == " ":
                statu = "blank"
            elif char in "+-":
                statu = "sign"
            elif char == ".":
                statu = "dot"
            elif char in "Ee":
                statu = "Ee"
            elif char in "0123456789":
                statu = "digit"
            else:
                return False
            
            if statu not in status[now]:
                return False
            now = status[now][statu]
        
        return now in (2, 3, 7, 8)
