from marshmallow import fields
from api import ma
from ..models import package_model


class PackageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = package_model.Package
        load_instance = True
        fields = ("id", "name", "version")

    name = fields.String(required=True)
    #packages = fields.List(fields.Nested(package_schema.PackageSchema), required=True)
