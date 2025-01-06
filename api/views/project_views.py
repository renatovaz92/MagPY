from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from ..entities import project
from ..services import project_service,package_service
from ..models import package_model,project_model
from ..schemas import project_schema
import urllib3

headers = urllib3.HTTPHeaderDict()
headers.add("Accept","application/json")
headers.add("Content-type","application/json")


class ProjectList(Resource):

    def get(self):
        prjcts = project_service.read_projects()
        prjcts_schema = project_schema.ListProjectSchema(many=True)
        return make_response(prjcts_schema.jsonify(prjcts),200)
    
    def post(self):

        has_not_version = None
        proj_sch = project_schema.ProjectSchema()
        validate = proj_sch.validate(request.json)
        package_objs = []
        if validate:
            return make_response(jsonify(validate),400)
        else:
            name = request.json["name"]
            packages = request.json["packages"]

            for pckgs in packages:
                validate_packages = "https://pypi.org/pypi/" + pckgs["name"] + "/json"
                response_validate = urllib3.request("GET",validate_packages,headers=headers)

                if "version" in pckgs:
                    validate_packages_version = "https://pypi.org/pypi/" + pckgs["name"] + "/" + pckgs["version"] + "/json"
                    response_validate_version = urllib3.request("GET",validate_packages_version,headers=headers)
                    if response_validate_version.status == 404:
                        has_not_version = True
                    else:
                        has_not_version = False

                if response_validate.status == 404 or has_not_version == True:
                    return make_response(jsonify("""{"error": "One or more packages doesn't exist"}"""), 400)

                else:

                    if "version" in pckgs:
                        name_package = pckgs["name"]
                        version_package = pckgs["version"]
                        new_package = package_model.Package(
                            name=name_package,
                            version=version_package
                        )
                        package_service.create_package(new_package)

                        pack_obj = package_service.read_package_and_version(pckgs["name"],pckgs["version"])
                        package_objs.append(pack_obj)

                    else:
                        name_package = pckgs["name"]
                        search_package_version = "https://pypi.org/pypi/" + name_package + "/json"
                        response = urllib3.request("GET",search_package_version,headers=headers)
                        data = response.json()
                        pkcg_url = data["info"]
                        version_package = str(pkcg_url["version"])
                        new_package = package_model.Package(
                            name=name_package,
                            version=version_package
                        )
                        package_service.create_package(new_package)

                        pack_obj = package_service.read_package_and_version(pckgs["name"], version_package)
                        package_objs.append(pack_obj)

            new_project = project_model.Project(
               name=name,
               packages=package_objs
            )

            project_service.create_project(new_project)
            project_name = project_service.read_project_name(name)
            pn = project_schema.ListProjectSchema()
            return make_response(pn.jsonify(project_name), 200)

class ProjectDetail(Resource):

    def get(self, name):
        project = project_service.read_project_name(name)
        if project is None:
            return make_response(jsonify("Project was not found."), 404)
        prjct_schema = project_schema.ListProjectSchema()
        return make_response(prjct_schema.jsonify(project),200)


    def delete(self, name):
        project_bd = project_service.read_project_name(name)
        if project_bd is None:
            return make_response(jsonify("Project was not found."), 404)
        project_service.delete_project(project_bd)
        return make_response(jsonify("Project was deleted with success."), 200)



api.add_resource(ProjectList, '/api/projects')
api.add_resource(ProjectDetail,'/api/projects/<string:name>')