import datetime

class RoboDog:
    __name = "RoboDog"
    __val1 = 0
    __val2 = 0
    __result = None
    __greeting = ["おはよう", "こんにちは", "こんばんは"]

    def __init__(self, name: str):
        self.name = name

    # ゲッターセッター
    def setName(self, name: str):
        self.name = name
    def getName(self) -> str:
        return self.name

    def setVal1(self, val: int):
        self.val1 = val
    def getVal1(self) -> int:
        return self.val1
    
    def setVal2(self, val: int):
        self.val2 = val
    def getVal2(self) -> int:
        return self.val2
    
    def setResult(self, result: int):
        self.result = result
    def getResult(self) -> int:
        return self.result
    
    # 時刻に応じた挨拶をします
    def getGreeting(self) -> str:
        hour = datetime.datetime.now().hour
        if 5 <= hour < 11:
            return self.__greeting[0]
        elif 11 <= hour < 18:
            return self.__greeting[1]
        else:
            return self.__greeting[2]

    # 足し算をします
    def calc(self) -> int:
        self.result = self.val1 + self.val2
        return self.result