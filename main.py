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

if __name__ == "__main__":
    main()