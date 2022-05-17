# Import de librerias necesarias
from datetime import date
from tkinter.filedialog import SaveAs

# Import de modulos
import calculo_horas

# Declaracion de algunas clases y funciones
class Empleado:
    def __init__(self, nombre: str, apellido: str, dob: date) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.dob = dob

    # Metodo para calculo de edad
    def edad(self) -> int:
        now = date.today()
        edad = now.year - self.dob.year - ((now.month, now.day) <
               (self.dob.month, self.dob.day))
        return edad

    # Metodo para saber donde trabaja
    def puesto(self, puesto: str, lang: list, nivel: list) -> str:
        result = ''
        result += f'{puesto}\n'
        for l, n in zip(lang, nivel): 
            result += f'Lenguaje: {l} - Nivel: {n}\n'
        return result.rstrip('\n')

    # Metodo para saber el salario en ARS
    def salario(self, salario_usd: float) -> float:
        tipo_de_cambio = 115.43
        salario_usd = salario_usd * tipo_de_cambio
        return salario_usd

# Ejecucion de programa
def main():
    nombre = 'Cesar'
    apellido = 'Aracena'
    dob = '15/08/1979'

    cesar = Empleado(nombre, apellido, date(int(dob.split('/')[2]), int(dob.split('/')[1]), int(dob.split('/')[0])))
    edad = cesar.edad()
    puesto = cesar.puesto('Desarrollador', ['Python', 'PHP'], ['Senior', 'Ssr'])
    salario = cesar.salario(1_000)

    print('Ficha de empleado:')
    print('######################')
    print(f'Nombre: {nombre.capitalize()}')
    print(f'Apellido: {apellido.capitalize()}')
    print(f'Fecha de Nac.: {dob} ({edad} años)')
    print(f'Puesto: {puesto}')
    print(f'Horas trabajadas por semana: {calculo_horas.calc(8.7, 4)}')
    print(f'Salario: ARS$ {salario:,}')

if __name__ == '__main__':
    main()
