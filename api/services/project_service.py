from api import db
from ..models import project_model

def create_project(project):
    db.session.add(project)
    db.session.commit()
    db.session.close()
    return project

def read_projects():
    projects = project_model.Project.query.all()
    return projects

def read_project_name(name):
    project = project_model.Project.query.filter_by(name=name).first()
    return project

def delete_project(project):
    db.session.delete(project)
    db.session.commit()