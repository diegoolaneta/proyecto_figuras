def get_identificador() -> str:
	return "rectángulo"

def get_area(base:int, altura: int) -> int:
	area = base*altura
	return area

def get_perimetro(base:int, altura: int) -> int:
	perimetro = 2*base + 2*altura
	return perimetro
