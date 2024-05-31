import allure
from src.operaciones import sumar, restar, promediar

@allure.epic("Operaciones matemáticas")
@allure.feature("Operaciones matemáticas")
@allure.description("Test donde se calcula la suma, la resta y el promedio de numeros")
def test_sumar():
    resultado = sumar(2,2)
    assert resultado == 4

def test_restar():
    resultado = restar(2,2)
    assert resultado == 0

def test_promediar():
    numeros = [2,2,2,2]
    resultado = promediar(numeros)
    assert resultado == 2
