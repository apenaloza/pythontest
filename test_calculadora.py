from calculadora import sumar, restar

def test_sumar():
    assert sumar(2,3) ==5
    assert sumar(-1,1) == 0

def test_restar():
    assert restar(5,3) ==2
    assert restar(10,5) == 5


