from Project import ma
from Project.Users.models import Usuario

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Usuario
        load_instance = True
        #load_only= ('password', )
        

Usuario_Schema = UsuarioSchema()


class LoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True


login_Schema = LoginSchema(partial=True, unknown=False, only=("correo","password"))