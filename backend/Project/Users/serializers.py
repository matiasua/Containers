from Project import ma
from Project.Users.models import Usuario

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Usuario
        load_instance = True
        load_only= ('password', )
        

Usuario_Schema = UsuarioSchema()