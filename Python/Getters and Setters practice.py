class MyClass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"Value is {self._value}")

    # GETTER
    @property
    def ten_value(self):
        return 10* self._value
    
    # SETTER
    @ten_value.setter
    def ten_value(self, new_value):
        self._value=new_value/10
        return 10* self._value
    
obj = MyClass(10)
obj.ten_value=67
print(obj.ten_value)
obj.show()