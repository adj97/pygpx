import datetime

class xmldatetime:

    def __init__(self,dt):
        self.year = int(dt.split("T")[0].split("-")[0])
        self.month = int(dt.split("T")[0].split("-")[1])
        self.day = int(dt.split("T")[0].split("-")[2])
        self.hour = int(dt.split("T")[1].split(":")[0])
        self.minute = int(dt.split("T")[1].split(":")[1])
        self.second = int(dt.split("T")[1].split(":")[2].split(".")[0])
        self.msecond = int(dt.split("T")[1].split(":")[2].split(".")[0].split("Z")[0])

        self.dt = datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second, self.msecond)

    def toXmlString(self):
        T = "T"
        Z = "Z"
        format = "%Y-%m-%d" + T + "%H:%M:%S.%f"
        output = self.dt.strftime(format)[:-3] + Z
        print(output)
        return  output

    def __sub__(self, other):
        return self.dt-other.dt