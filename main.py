import time

from big_int import BIG_INT


def main():
    def multiply_big_ints(big_int_list1:list[int], big_int_list2:list[int])->str:
        big_int1:BIG_INT=BIG_INT(big_int_list=big_int_list1)
        # print(f"big_int_list1_value: {big_int1.value}")
        # big_int2:BIG_INT=BIG_INT(big_int_list=big_int_list2)
        return big_int1.multiply(value_list=big_int_list2)
    print(multiply_big_ints([88], [88])) # expected output: 7744
    print(multiply_big_ints([123456790, 123456790], [123456790, 123456790]))
    # expected output: 1524157878067367851562262075019052100
    big_int_2=BIG_INT(big_int_list=[2])
    print(f"2^20 = {big_int_2.power(20)}") # expected output: 1048576
    print(f"2^50 = {big_int_2.power(50)}") # expected output: 1125899906842624
    print(f"2^100 = {big_int_2.power(100)}") # expected output: 1267650600228229401496703205376
    print(f"2^10000 = {big_int_2.power(10000)}") 
    #expected output: 107150860718626732094842504906000181056140481170553360744375038837035105112493612249319837881569585812
    # 75946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046
    # 474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
    time_taken=time.time()
    big_int_2.power(100000)
    print(f"Time taken to compute 2^100000: {time.time()-time_taken} seconds")

if __name__ == "__main__":
    main()