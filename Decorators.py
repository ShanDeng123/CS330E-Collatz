def my_power(outside_function):
    def sq_function(outside_value):

        outside_value = outside_function(outside_value)
        outside_value = outside_value**2
        return outside_value

    return sq_function
        

@my_power
def func1(n):
   print('func1 is executing!') 
   return n * n

@my_power
def func2(n):
   print('func2 is executing!')
   return n + n

def test_my_power () :
   print("Output: my_power()")
   print(func1(2))
   print(func2(1))

test_my_power()
