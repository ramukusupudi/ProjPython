from typing import List

def rolling_average(values: List,period:int)-> List:
    rolling_average = []
    for i in range(period,len(values)+1):
        average=sum(values[i-period:i])/period
        rolling_average.append(average)

    return rolling_average
    