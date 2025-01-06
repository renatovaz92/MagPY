from api import db


class Package(db.Model):
    __tablename__ = "package"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    version = db.Column(db.String(50))
    projects = db.relationship("Project", secondary="package_project", back_populates="packages")
