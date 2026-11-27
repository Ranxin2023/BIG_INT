from __future__ import annotations


class BIG_INT:

    def __init__(self, big_int_list:list[int] | None=None, int_value:int | None=None) ->None:
        self.UNIT=10**9
        self.MAX_INT=2**32-1
        self.INT_LIMIT=2**64-1
        self.value:list[int]=[]
        if big_int_list is not None:
            self.value:list[int]=big_int_list[:]
        elif int_value is not None:
            self.value:list[int]=[]
            while int_value>0:
                self.value.append(int_value%self.UNIT)
                int_value//=self.UNIT
        else:
            self.value:list[int]=[0]

    # convert to string
    def __str__(self) ->str:
        return self.to_string(value_list=self.value)
    
    def to_string(self, value_list:list[int])->str:
        if len(value_list)==0:
            return "0"
        res:str=str(value_list[-1])
        for _int in value_list[-2::-1]:
            res+=str(_int).zfill(9)
        return res

    # remove leading zeros
    def remove_leading_zeros(self, value_list:list[int])->None:
        while len(value_list)>1 and value_list[-1]==0:
            value_list.pop()

    def add_helper(self, value_list1:list[int], value_list2:list[int])->list[int]:
        max_len:int=max(len(value_list1), len(value_list2))
        result:list[int]=[0]*(max_len+1)
        for i in range(max_len):
            if i<len(value_list1):
                result[i]+=value_list1[i]
            if i<len(value_list2):
                result[i]+=value_list2[i]
            if result[i]>=self.UNIT:
                result[i+1]+=result[i]//self.UNIT
                result[i]%=self.UNIT
        self.remove_leading_zeros(value_list=result)
        return result
    
    def add(self, value_list:list[int])->str:
        result:list[int]=self.add_helper(value_list1=self.value, value_list2=value_list)
        self.value=result
        return str(self)
    
    def multiply_helper(self, value_list1:list[int], value_list2:list[int])->list[int]:
        # reverse_value1:list[int]=value_list1[::-1]
        # reverse_value2:list[int]=value_list2[::-1]
        result:list[int]=[0]*(len(value_list1)+len(value_list2))
        for i in range(len(value_list1)):
            for j in range(len(value_list2)):
                result[i+j]+=value_list1[i]*value_list2[j]
                if result[i+j]>=self.UNIT:
                    result[i+j+1]+=result[i+j]//self.UNIT
                    result[i+j]%=self.UNIT
        self.remove_leading_zeros(value_list=result)
        return result

    # multiply two big integers
    def multiply(self, value_list:list[int])->str:
        result:list[int]=self.multiply_helper(value_list1=self.value, value_list2=value_list)
        self.value=result
        return str(self)

    def power_helper(self, base: list[int], exponent: int) -> list[int]:
        if exponent == 0:
            return [1]
        elif exponent == 1:
            return base
        else:
            half_power = self.power_helper(base, exponent // 2)
            result = self.multiply_helper(half_power, half_power)
            if exponent % 2 == 1:
                result = self.multiply_helper(result, base)
            return result
    def power(self, exponent:int)->str:
        result:list[int]=self.power_helper(base=self.value, exponent=exponent)
        return self.to_string(value_list=result)

    def factorial(self, n:int)->str:
        if n==0 or n==1:
            return "1"
        result:list[int]=[1]
        for i in range(2, n+1):
            result=self.multiply_helper(result, [i])
        return self.to_string(value_list=result)