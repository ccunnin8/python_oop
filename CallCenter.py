class Call(object):
    def __init__(self,id,name,number,time,reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason= reason

    def __str__(self):
        return "id: {x}\nname: {y}\nnumber: {z}\ntime: {a}\nreason: {b}".format(x=self.id,y=self.name,z=self.number,a=self.time,b=self.reason)


class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.qsize = 0

    def add(self,call):
        self.calls.append(call)
        self.qsize += 1
        return self

    def remove(self,id):
        for index, call in enumerate(self.calls):
            if call.id == id:
                del(self.calls[index])
                self.qsize -= 1
                return self
        return self

    def info(self):
        print(self.qsize)
        for call in self.calls:
            print(call)
