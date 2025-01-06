from ..models import package_model
from api import db

def create_package(package):
    package_db = package_model.Package(name=package.name,version=package.version)
    db.session.merge(package_db)
    db.session.commit()
    db.session.close()
    return package_db

def read_package_and_version(package, version):
    package_and_version = package_model.Package.query.filter_by(name=package,version=version).first()
    return package_and_version
