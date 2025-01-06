from api import ma
from ..models import project_model
from marshmallow import fields
from ..schemas import package_schema

class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = project_model.Project
        load_instance = True
        fields = ("id","name","packages")
    
    name = fields.String(required=True)
    packages = fields.List(fields.Nested(package_schema.PackageSchema), required=True)

class ListProjectSchema(ma.SQLAlchemyAutoSchema):
    packages = ma.Nested(package_schema.PackageSchema, many=True, only=("name","version"))

    class Meta:
        model = project_model.Project
        load_instance = True
        fields = ("id", "name", "packages")

    name = fields.String(required=True)
