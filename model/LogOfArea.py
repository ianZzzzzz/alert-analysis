class LogOfArea: 
    device_id: 0
    timestamp: 0

    def __init__(self, raw):
        self.device_id = raw[0]
        self.timestamp = raw[1]
    

class LogOfAreaList:
    data: []

    def __init__(self, data=[]):
        self.data = data
    
    def pushLogOfArea(logOfArea):
        self.data.append(logOfArea)

    def groupByArea():
        # self.data = self.data.sort(x:x)
        return

    def groupById():
        return
    
    def getTimeBetween():
        return

    def pluckDataBy(key, chunck):
        return
line = ['c1','c2']

# 1. read raw data from csv
# 2. upgrade raw data -> LogOfAreaList
logOfAreaList =  LogOfAreaList()
logOfArea =  LogOfArea(line)
#logOfAreaList.pushLogOfArea(logOfArea)

