class Day:
    def __init__(self,day,obj1,obj2,obj3,obj4):
        self.day=day
        self.obj1=obj1
        self.obj2=obj2
        self.obj3=obj3
        self.obj4=obj4
        
        
    def __str__(self):
        s=""
        s+=self.day+"\n"
        table = {'9:00': self.obj1, '10:50': self.obj2, '12:40': self.obj3,
                 '14:30': self.obj4}
        for time, obj in table.items():
            s+=str('%-10s  %10s' % (time, obj))
            s+="\n"
        return s



class All:
    def __init__(self,days):
        self.days=days
    def __str__(self):
        s2="Это все расписания, которые есть в памяти: "+"\n"
        s2+="18704: "+"\n"
        for i in range(len(self.days)):
            for j in range(len(self.days[i])):
                s2+=str(self.days[i][j])
                s2+="\n"
        return s2
    def __repr__(self):
        return self.__str__()
        
