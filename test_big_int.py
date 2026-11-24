from big_int import BIG_INT


def test_init():
    a = BIG_INT(int_value=1000000002)
    assert a.value == [2, 1]


def test_to_string():
    a = BIG_INT(big_int_list=[123, 456, 789])
    assert str(a) == "789000000456000000123"


def test_multiply():
    a = BIG_INT(int_value=1234567890123456789)
    b = BIG_INT(int_value=9876543210987654321)

    assert a.multiply(b.value) == str(
        1234567890123456789 * 9876543210987654321
    )


def test_power():
    a = BIG_INT(int_value=123456789)

    assert a.power(10) == str(123456789 ** 10)


def test_zero():
    a = BIG_INT(int_value=0)

    assert str(a) == "0"
    assert a.multiply([123]) == "0"
    assert a.power(10) == "0"


def test_power_zero():
    a = BIG_INT(int_value=123)

    assert a.power(0) == "1"