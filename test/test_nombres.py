import allure
from src.nombres import obtener_nombres_frutas

@allure.epic("Listas de nombres")
@allure.feature("Frutas")
@allure.description("Test donde se devuelve una lista de nombres de frutas")
def test_obtener_nombres_frutas():
    nombres = obtener_nombres_frutas()
    assert isinstance(nombres, list)
