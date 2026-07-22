class Solution:
    def isNumber(self, s):
        try:
            x = float(s)
            if s.lower() in ["inf", "+inf", "-inf", "infinity", "+infinity", "-infinity", "nan"]:
                return False
            return True
        except:
            return False
