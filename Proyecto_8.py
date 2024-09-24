print("Este programa esta diseñado para optimizar la gestion y organizacion de los hospitales, falicitara el registro y monitoreo de la informacion clinica de cada paciente .")

from datetime import datetime

class datos_de_Pacientes:
    def __init__(self, nombre, fecha_nacimiento, genero, padecimientos=None, alergias_medicamentos=None, historial_medico=None):
        self.nombre = nombre
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
        self.genero = genero
        self.padecimientos = padecimientos if padecimientos else []
        self.alergias_medicamentos = alergias_medicamentos if alergias_medicamentos else []
        self.historial_medico = historial_medico if historial_medico else []
        self.citas = []
# definimos self para que apareciera como listado en los datos del paciente
        hoy = datetime.today()
        edad = hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return edad
#estamos difiniendo agregar_citas con self que es el comando  para ser el listado para saber la hora  la fecha  de la cita del paciente
    def agregar_cita(self, fecha, hora):
        self.citas.append({'fecha': fecha, 'hora': hora})

    def agregar_padecimiento(self, padecimiento):
        self.padecimientos.append(padecimiento)

    def agregar_alergia_medicamento(self, alergia):
        self.alergias_medicamentos.append(alergia)

    def agregar_historial_medico(self, historial):
        self.historial_medico.append(historial)
#esto es para mostrar el historial del paciente poniendo "f" para facilitar la escritura  y inprimiendolo ala pantalla la informacion de los pacientes
    def mostrar_info(self):
        print(f'Nombre del paciente: {self.nombre}')
        print(f'Edad del paciente: {self.calcular_edad()}')
        print(f'Género del paciente: {self.genero}')
        print("Padecimientos/Enfermedades:")
        for padecimiento in self.padecimientos:
            print(f'- {padecimiento}')
        print("Alergias a Medicamentos:")
        for alergia in self.alergias_medicamentos:
            print(f'- {alergia}')
        print("Historial Médico:")
        for historial in self.historial_medico:
            print(f'- {historial}')
        print("Citas Programadas:")
        for cita in self.citas:
            print(f'{cita["fecha"]} a las {cita["hora"]}')
#aqui es para registrar al paciente con sus datos  con un return para que se regrese al menu del incicio
def registrar_paciente():
    nombre = input("¿Cuál es el nombre del paciente? ")
    fecha_nacimiento = input("¿Cuál es la fecha de nacimiento del paciente? (DD/MM/AAAA): ")
    genero = input("Género del paciente: ")
    padecimientos = input("Padecimientos del paciente (separados por comas): ").split(',')
    alergias_medicamentos = input("Alergias a medicamentos (separadas por comas): ").split(',')
    historial_medico = input("Historial médico del paciente (separado por comas): ").split(',')
    return datos_de_Pacientes(nombre, fecha_nacimiento, genero, padecimientos, alergias_medicamentos, historial_medico)
#esto es para actualizar la informacion del paciente ya registrado  y usamos el comando datetime.strptime para que cada año se valla sumando al registro del paciente
def actualizar_paciente(paciente):
    print("Actualizando la información del paciente: ")
    paciente.nombre = input("Nombre del paciente: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD/MM/AAAA): ")
    paciente.fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
    paciente.genero = input("Género: ")
    padecimientos = input("Padecimientos del paciente (separados por comas): ").split(',')
    paciente.padecimientos = padecimientos
    alergias_medicamentos = input("Alergias a medicamentos (separadas por comas): ").split(',')
    paciente.alergias_medicamentos = alergias_medicamentos
    historial_medico = input("Historial médico del paciente (separado por comas): ").split(',')
    paciente.historial_medico = historial_medico
#
def programar_cita(paciente):
    fecha = input("Fecha de la cita (DD/MM/AAAA): ")
    hora = input("Hora de la cita (HH:MM): ")
    paciente.agregar_cita(fecha, hora)

def mostrar_pacientes(pacientes):
    if not pacientes:
        print("No hay registro de pacientes")
        return None
    else:
        for i, paciente in enumerate(pacientes):
            print(f'{i + 1}. {paciente.nombre}')
        return pacientes

def main():
    pacientes = []
    while True:
        print("\nMenú Principal")
        print("1. Registrar Paciente")
        print("2. Actualizar Información del Paciente")
        print("3. Programar Cita")
        print("4. Consultar Información del Paciente")
        print("5. Salir")
        opción = input("Seleccione una opción: ")

        if opción == "1":
            paciente = registrar_paciente()
            pacientes.append(paciente)
        elif opción == "2":
            if mostrar_pacientes(pacientes) is not None:
                index = int(input("Seleccione el número del paciente a actualizar: ")) - 1
                if 0 <= index < len(pacientes):
                    actualizar_paciente(pacientes[index])
                else:
                    print("Selección inválida.")
        elif opción == "3":
            if mostrar_pacientes(pacientes) is not None:
                index = int(input("Seleccione el número del paciente: ")) - 1
                if 0 <= index < len(pacientes):
                    programar_cita(pacientes[index])
                else:
                    print("Selección inválida.")
        elif opción == "4":
            if mostrar_pacientes(pacientes) is not None:
                index = int(input("Seleccione el número del paciente: ")) - 1
                if 0 <= index < len(pacientes):
                    pacientes[index].mostrar_info()
                else:
                    print("Selección inválida.")
        elif opción == "5":
            print("Saliendo del programa...")
            print("Gracias por visitarnos al hospital chancludo")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    main()
