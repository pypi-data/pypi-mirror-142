from dataclasses import dataclass


@dataclass
class Indicator:
    Id: str
    Name: str
    Script: str
    FirstLevel: str
    SecondLevel: str


@dataclass
class SuperTrend(Indicator):
    Value_1: float
    Value_2: float

    def __init__(self, Value_1: float = 0, Value_2: float = 0):
        super().__init__(Id="STD;Supertrend",
                         Name="SuperTrend",
                         Script="Script@tv-scripting-101!",
                         FirstLevel="",
                         SecondLevel="")
        self.Value_1 = Value_1
        self.Value_2 = Value_2


@dataclass
class Volume(Indicator):
    Value_1: float
    Value_2: float

    def __init__(self, Value_1: float = 0, Value_2: float = 0):
        super().__init__(Id="",
                         Name="Volume",
                         Script="Volume@tv-basicstudies-150",
                         FirstLevel="",
                         SecondLevel="")
        self.Value_1 = Value_1
        self.Value_2 = Value_2


@dataclass
class TripleMovingAverages(Indicator):
    Value_1: float
    Value_2: float
    Value_3: float

    def __init__(self, Value_1: float = 0, Value_2: float = 0, Value_3: float = 0):
        super().__init__(Id="PUB;y784PkOKflCjfhCiCB4ewuC0slMtB8PQ",
                         Name="TripleMovingAverages",
                         Script="Script@tv-scripting-101!",
                         FirstLevel="",
                         SecondLevel="")
        self.Value_1 = Value_1
        self.Value_2 = Value_2
        self.Value_3 = Value_3


@dataclass
class MovingAverageExponential(Indicator):
    Value_1: float

    def __init__(self, Value_1: float = 0):
        super().__init__(Id="STD;EMA",
                         Name="MovingAverageExponential",
                         Script="Script@tv-scripting-101!",
                         FirstLevel="",
                         SecondLevel="")
        self.Value_1 = Value_1


@dataclass
class MovingAverage(Indicator):
    Value_1: float

    def __init__(self, Value_1: float = 0):
        super().__init__(Id="STD;SMA",
                         Name="MovingAverage",
                         Script="Script@tv-scripting-101!",
                         FirstLevel="",
                         SecondLevel="")
        self.Value_1 = Value_1


@dataclass
class ATR_StopLossFinder(Indicator):
    Value_1: float
    Value_2: float

    def __init__(self, Value_1: float = 0, Value_2: float = 0, ):
        super().__init__(Id="PUB;d48234236f7345c09e3d9017f8c31070",
                         Name="ATR_StopLossFinder",
                         Script="Script@tv-scripting-101!",
                         FirstLevel="",
                         SecondLevel="")
        self.Value_1 = Value_1
        self.Value_2 = Value_2

@dataclass
class Sell_Buy_Rates(Indicator):
    Value_1: float
    Value_2: float

    def __init__(self, Value_1: float = 0, Value_2: float = 0, ):
        super().__init__(Id="PUB;LzjHUC8QDN1HzufYCSLfxaV4b9yR6TMx",
                         Name="Sell_Buy_Rates",
                         Script="Script@tv-scripting-101!",
                         FirstLevel="",
                         SecondLevel="")
        self.Value_1 = Value_1
        self.Value_2 = Value_2

@dataclass
class CM_Williams_Vix_Fix(Indicator):
    Value_1: float
    Value_2: float

    def __init__(self, Value_1: float = 0, Value_2: float = 0, ):
        super().__init__(Id="PUB;239",
                         Name="CM_Williams_Vix_Fix",
                         Script="Script@tv-scripting-101!",
                         FirstLevel="",
                         SecondLevel="")
        self.Value_1 = Value_1
        self.Value_2 = Value_2