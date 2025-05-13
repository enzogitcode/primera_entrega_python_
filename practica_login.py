# Consigna
# Para tu primera entrega, te proponemos que crees un programa que permita emular el registro y almacenamiento de usuarios en una base de datos. Hazlo utilizando el concepto de funciones, diccionarios, bucles y condicionales.

# Objetivos
# Practicar el concepto de funciones.

# Desarrollar la parte lógica para el registro de usuarios.

# Requisitos
# Diccionarios (guardado de datos)

# Input (solicitud de datos)

# Variables

# If (chequeo de datos)

# While (iteración para el programa, sea para agregar, loguear o mostrar)

# For (recorrer datos y para búsqueda)

# Print

# Funciones separadas para registro, almacenamiento y muestra

# Recomendaciones
# El formato de registro es: Nombre de usuario y Contraseña.

# Utilizar una función para almacenar la información y otra función para mostrar la información.

# Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).

# Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.

# Formato
# El proyecto debe compartirse utilizando Colab bajo el nombre “ArmaTuLogin+Apellido”, por ejemplo “ArmaTuLogin+Fernandez”

##Armando el login
##base de datos vacía
BD= []

##clase user
class User:
    def __init__(self, name, password):
        self.name= name
        self.password= password
    
    ##validar contraseña
    @staticmethod
    def name_validator(name):
        alphanum= name.isalpha()
        return len(name) > 0 and alphanum == True
    def password_validator(password):
        return len(password) > 0

#función para crear nuevo usuario
def create_new_user():
    new_user= {}
    if BD ==[]:
        if new_user == {}: 
            name= input('username: \n')
            while User.name_validator(name) == False:
                print('el nombre no puede estar vacío y no puede contener números')
                name= input('username: \n')
            else:
                password= input('password: \n')
                User.password_validator(password)
                while User.password_validator(password) == False:
                    print('la contraseña no puede estar vacía')
                    password= input('password: \n')
                else:
                    new_user["name"]= name
                    new_user['password']= password
                    save_new_user(new_user)
                    print(f'Nuevo usuario creado: {new_user["name"]}')
                    main()
    else: 
        if new_user == {}: 
            name= input('username: \n')
            while User.name_validator(name) == False:
                print('el nombre no puede estar vacío y no puede contener números')
                name= input('username: \n')
            else:
                password= input('password: \n')
                User.password_validator(password)
                while User.password_validator(password) == False:
                    print('la contraseña no puede estar vacía')
                    password= input('password: \n')
                else:
                    new_user["name"]= name
                    new_user['password']= password
                    save_new_user(new_user)

def save_new_user(new_user):
    print(f'Nuevo usuario creado: {new_user['name']}')
    BD.append(new_user)

def login_password_validator(name, BD):
        for i in BD:
            if i["name"] == name:
                password_correcta= (i["password"])
        return password_correcta

def login():
    name= input('Escribe el nombre del usuario: \n')
    nombres= []
    for i in range(len(BD)):
        nombres.append(BD[i]['name'])
    if name not in nombres:
        print('El usuario no existe')
        name= input('Escribe el nombre del usuario: \n')
    else:
        password= input('Escribe el password: \n')
        correct_password= login_password_validator(name, BD)
        while password != correct_password:
            print('Contraseña incorrecta')
            password= input('Escribe el password: \n')
        else:
            print('Acceso correcto, usuario Logueado')

def main():
    if BD == []:
        print("""
              Elige una opción: 
              opción r= Registrarse
              opción s= Salir
""")
        opc= input('Escribe r o s \n')
        match opc:
            case 'r':
                create_new_user()
            case 's':
                print('Muchas gracias! Vuelva Pronto!')
            case _:
                print('Elige una opción correcta')
                opc= input('Escribe r o s  \n')
    else:
        print("""¿Desea crear otro usuario? O acceder al login? 
       opción 's'= Crear otro usuario
        opción 'n'= Salir
              opción 'l'= acceder al login

               """)
        opc= input('\n')
        match opc:
            case 's':
                create_new_user()
                main()
            case 'n':
                print('Muchas gracias! vuelva pronto!')
            case 'l':
                login()
            case _:
                print('Elige una opción válida')
                opc= input('Escribe "y" para crear otro o "n" para salir \n')

main()