from Project.Users._testsUser.configTests import configTests
from Project.Users.models import Usuario
from Project.Users.serializers import Usuario_Schema
import Project.Users._testsUser.utils as utils

class CreateTestCase(configTests):
    def test_create_user(self):

        data = utils.allDataUser()
        response = self.client.post(
            '/register',
            json=data
        )
        self.assertStatus(response, 201)
        userCount = Usuario.query.count()
        self.assertEquals(1, userCount)


    def test_create_user_no_data(self):

        data = {}
        response = self.client.post(
              '/register',
              json=data 
        )
        self.assertStatus(response, 400)


    def test_create_user_diff_pass(self):
        data = utils.diff_pass()
        response = self.client.post(
            '/register',
            json=data
        )
        self.assertStatus(response, 400)
        self.assertEquals(response.get_json() , 'Contraseña no coincide')

# 1 - Ingreso todos los datos del usuario
# 2 - No ingreso ningun campo
# 3 - Ingreso contraseñas diferentes        
      


  