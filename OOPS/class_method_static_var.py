#static variable

'''class A:
    var = 10

    def __init__(self):
        pass

    def f1(self):
        print('Hii Treenetra')

    @classmethod
    def chinu(cls):
        print(cls.var)
        cls.f1('iykyk')



obj1 = A
obj1.chinu()'''


#Static Method

class A:

    @staticmethod
    def fib_series(num):
        li=[0,1] #local variable
        for i in range(num):
            generate_fib_num = li[-1]+li[-2]
            li.append(generate_fib_num)
        return li

    @classmethod
    def fib_mean(cls):
        fib = cls.fib_series(10)
        result_mean = sum(fib)/len(fib)
        return result_mean,fib

obj = A
print(obj.fib_mean())
