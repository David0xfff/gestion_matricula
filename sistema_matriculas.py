# sistema_matriculas.py

class SistemaMatriculas:
    def __init__(self):
        self.estudiantes = []
        self.cursos = {"Matemáticas": 20, "Ciencias": 15}

    def matricular_estudiante(self, nombre, curso):
        if curso in self.cursos and self.cursos[curso] > 0:
            self.estudiantes.append({"nombre": nombre, "curso": curso})
            self.cursos[curso] -= 1
            return f"{nombre} matriculado en {curso}."
        else:
            return "Cupo no disponible o curso no encontrado."

    def generar_factura(self, nombre, curso):
        if any(est["nombre"] == nombre and est["curso"] == curso for est in self.estudiantes):
            return f"Factura generada para {nombre} en el curso {curso}."
        return "No se encontró al estudiante matriculado."

    def generar_reporte(self):
        return {"estudiantes": self.estudiantes, "cursos_disponibles": self.cursos}

# Ejemplo de uso
sistema = SistemaMatriculas()
print(sistema.matricular_estudiante("Juan", "Matemáticas"))
print(sistema.generar_factura("Juan", "Matemáticas"))
print(sistema.generar_reporte())
