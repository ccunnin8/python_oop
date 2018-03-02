class MathDojo(object):
    def __init__(self,total=0):
        self.total = total

    def add(self,*nums):
        for num in nums:
            if type(num) == list or type(num) == tuple:
                self.total += sum(num)
            else:
                self.total += num
        return self

    def subtract(self,*nums):
        for num in nums:
            if type(num) == list or type(num) == tuple:
                self.total -= sum(num)
            else:
                self.total -= num
        return self

    def result(self):
        print(self.total)
        return self.total
md = MathDojo()
print(md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).total)
