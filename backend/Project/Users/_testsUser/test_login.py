from Project.Users._testsUser.configTests import configTests
from Project.Users.models import Usuario
import Project.Users._testsUser.utils as utils

class Testlogin(configTests):

  def test_login_void_field(self):
    data = utils.login_void_field()

    response = self.client.post(
        '/login',
        json=data
    )
    self.assertIn('correo', data)
    self.assertIn('password', data)
    self.assertStatus(response, 400)

  def test_login_error_password(self):
    datalogin = utils.login_error_password()
    dataregister = utils.allDataUser()

    #Registrar Usuario
    response_register = self.client.post(
        '/register',
        json=dataregister
    )
    self.assertStatus(response_register, 201)
    
    #Logearse con usuario registrado
    response_login = self.client.post(
        '/login',
        json=datalogin
    )
    userRegister = Usuario.query.filter_by(correo=dataregister['correo']).first()

    self.assertNotEquals(userRegister.password, datalogin['password'])
    self.assertStatus(response_login, 400)


    # 1 - Login con campos vacios
    # 2 - Login con error de contraseña