
def allDataUser():
    data= {
        "nombre": "name_test",
        "password": "password_test",
        "confirmPassword": "password_test",
        "correo": "correo@test",
        "direccion": "direccion_test"
        }
    return data

def WithoutName():
    data = {
        "password": "password_test",
        "confirmPassword": "password_test",
        "correo": "correo@test",
        "direccion": "direccion_test"
    }

def diff_pass():
    data = {
        "nombre": "name_test",
        "password": "password_test",
        "confirmPassword": "password_diff",
        "correo": "correo@test",
        "direccion": "direccion_test"
    }
    return data

def login_void_field():
    data = {
        "correo": "",
        "password": "",
    }
    return data

def login_error_password():
    data = {
        "correo": "correo@test",
        "password": "error_password"
    }
    return data