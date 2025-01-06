from api import db
from .package_model import Package

package_project = db.Table('package_project',
                           db.Column('package_id', db.Integer, db.ForeignKey('package.id'), primary_key=True, nullable=False),
                           db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True, nullable=False)
                           )


class Project(db.Model):
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    packages = db.relationship(Package, secondary="package_project", back_populates="projects")