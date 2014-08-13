__author__ = 'jburks'

from flask import Flask, jsonify, url_for
from flask.ext.restful import Api, Resource, abort
from model import *

app = Flask(__name__)
api = Api(app)


# API functions
class Terms(Resource):
    def get(self):
        terms = []
        for term in TermNames.select().where(TermNames.active == True):
            terms.append({
                "id": term.id,
                "term_name": term.term_name,
                "uri": api.url_for(Term, term_id=term.id)
            })

        return jsonify({"terms": terms})


class Term(Resource):
    def get(self, term_id):
        try:
            term = TermNames.get(TermNames.id == term_id)

            return jsonify({
                "term": [{
                             "id": term.id,
                             "term_name": term.term_name
                         }]
            })
        except:
            return abort(400, message="No such term")


class DeptsByTerm(Resource):
    def get(self, term_id):

        adoptions = Adoptions.select() \
                .join(Departments, JOIN_LEFT_OUTER) \
                .where(Adoptions.term_name == term_id) \
                .group_by(Departments) \
                .order_by(Departments.department_code)

        if adoptions.count() is not 0:
            departments = []
            for adoption in adoptions:
                departments.append({
                    "id": adoption.department.id,
                    "department_name": adoption.department.department_name,
                    "department_code": adoption.department.department_code
                })

            return jsonify({"departments": departments})

        else:
            return abort(400, message="No such term")

class CoursesByDept(Resource):
    def get(self, department_id):
        adoptions = Adoptions.select() \
                .join(Departments, JOIN_LEFT_OUTER) \
                .where(Adoptions.department == department_id)

        if adoptions.count() is not 0:
            courses = []
            for adoption in adoptions:
                courses.append({
                    "id": adoption.magento_course,
                    "department_name": adoption.department.department_name,
                    "department_code": adoption.department.department_code,
                    "course_name": adoption.course_name,
                    "course_code": adoption.course_code,
                    "section_code": adoption.section_code,
                    "course_materials_uri": api.url_for(MaterialsByCourseID, course_id=adoption.magento_course)
                })

            return jsonify({"courses": courses})
        else:
            return abort(400, message="No such department")


class CoursesByTerm(Resource):
    def get(self, term_id):
        adoptions = Adoptions.select().where(Adoptions.term_name == term_id)

        if adoptions.count() is not 0:
            courses = []
            for adoption in adoptions:
                courses.append({
                    "id": adoption.magento_course,
                    "department_name": adoption.department.department_name,
                    "department_code": adoption.department.department_code,
                    "course_name": adoption.course_name,
                    "course_code": adoption.course_code,
                    "section_code": adoption.section_code,
                    "course_materials_uri": api.url_for(MaterialsByCourseID, course_id=adoption.magento_course)
                })

            return jsonify({"courses": courses})
        else:
            return abort(400, message="No such term")


class SectionsByCourse(Resource):
    def get(self, department_id, course_code):

        adoptions = Adoptions.select() \
                .join(Departments, JOIN_LEFT_OUTER) \
                .where(Adoptions.course_code == course_code) \
                .where(Adoptions.department == department_id)

        if adoptions.count() is not 0:
            sections = []
            for adoption in adoptions:
                sections.append({
                    "id": adoption.magento_course,
                    "department_name": adoption.department.department_name,
                    "department_code": adoption.department.department_code,
                    "course_name": adoption.course_name,
                    "course_code": adoption.course_code,
                    "section_code": adoption.section_code,
                    "course_materials_uri": api.url_for(MaterialsByCourseID, course_id=adoption.magento_course)
                })

            return jsonify({"sections": sections})
        else:
            return abort(400, message="No such course")


def get_materials(course_id):
    adoptions = Adoptions.select(Adoptions, CatalogProductLink) \
        .join(Departments, JOIN_LEFT_OUTER) \
        .join(TermNames, JOIN_LEFT_OUTER, on=(Adoptions.term_name == TermNames.id)) \
        .switch(Adoptions).join(CatalogProductEntity, JOIN_LEFT_OUTER, on=(Adoptions.magento_course == CatalogProductEntity.entity).alias("product")) \
        .switch(Adoptions).join(CatalogProductLink, JOIN_LEFT_OUTER, on=(CatalogProductEntity.entity == CatalogProductLink.product).alias("link")) \
        .where(Adoptions.magento_course == course_id)

    materials = []
    for adoption in adoptions:
        # This is the ID of the book or "product" in Magento
        linked_product = adoption.link.linked_product.entity

        # Get the values for this product. Not as cool as a big single query, but hopefully faster.
        try:
            item_ean = CatalogProductEntityVarchar.get(
                CatalogProductEntityVarchar.entity == linked_product,
                CatalogProductEntityVarchar.attribute == eav_attr["item_ean"],
                CatalogProductEntityVarchar.store == 0)
            item_ean_value = item_ean.value
        except:
            item_ean_value = ""

        try:
            item_author = CatalogProductEntityVarchar.get(
                CatalogProductEntityVarchar.entity == linked_product,
                CatalogProductEntityVarchar.attribute == eav_attr["item_author"],
                CatalogProductEntityVarchar.store == 0)
            item_author_value = item_author.value
        except:
            item_author_value = ""

        try:
            item_title = CatalogProductEntityVarchar.get(
                CatalogProductEntityVarchar.entity == linked_product,
                CatalogProductEntityVarchar.attribute == eav_attr["item_title"],
                CatalogProductEntityVarchar.store == 0)
            item_title_value = item_title.value
        except:
            item_title_value = ""

        try:
            item_new = CatalogProductEntityVarchar.get(
                CatalogProductEntityVarchar.entity == linked_product,
                CatalogProductEntityVarchar.attribute == eav_attr["item_new"],
                CatalogProductEntityVarchar.store == 0)
            item_new_value = float(item_new.value)
        except:
            item_new_value = ""

        try:
            item_rental = CatalogProductEntityVarchar.get(
                CatalogProductEntityVarchar.entity == linked_product,
                CatalogProductEntityVarchar.attribute == eav_attr["item_rental"],
                CatalogProductEntityVarchar.store == 0)
            item_rental_value = float(item_rental.value)
        except:
            item_rental_value = ""

        try:
            item_used = CatalogProductEntityDecimal.get(
                CatalogProductEntityDecimal.entity == linked_product,
                CatalogProductEntityDecimal.attribute == eav_attr["item_used"],
                CatalogProductEntityDecimal.store == 0)
            item_used_value = float(item_used.value)
        except:
            item_used_value = ""

        try:
            no_text_required = CatalogProductEntityInt.get(
                CatalogProductEntityInt.entity == linked_product,
                CatalogProductEntityInt.attribute == eav_attr["no_text_required"],
                CatalogProductEntityInt.store == 0)
            no_text_required_value = no_text_required.value
        except:
            no_text_required_value = ""


        materials.append({
            "id": adoption.magento_course,
            "term_name": adoption.term_name.term_name,
            "term_id": adoption.term_name.id,
            "department_name": adoption.department.department_name,
            "department_code": adoption.department.department_code,
            "department_id": adoption.department.id,
            "course_name": adoption.course_name,
            "course_code": adoption.course_code,
            "section_code": adoption.section_code,
            "section_name": "",
            "section_instructor": "",
            "book_id": linked_product,
            "variant_id": linked_product,
            "title": item_title_value,
            "author": item_author_value,
            "isbn": item_ean_value,
            "required": no_text_required_value,
            "publisher": "",
            "edition_number": "",
            "copyright_year": "",
            "new_price": item_new_value,
            "new_cost": "",
            "new_inventory": "",
            "used_price": item_used_value,
            "used_cost": "",
            "used_inventory": "",
            "new_rental_price": item_rental_value,
            "new_rental_cost": "",
            "new_rental_inventory": "",
            "used_rental_price": item_rental_value,
            "used_rental_cost": "",
            "used_rental_inventory": "",
        })

    return materials

class MaterialsByCourseID(Resource):
    def get(self, course_id):
        try:
            adoption = Adoptions.select(Adoptions.magento_course).where(Adoptions.magento_course == course_id).get()
        except:
            return abort(400, message="No such course")

        try:
            return jsonify({"materials": get_materials(adoption.magento_course)})

        except:
            return abort(400, message="No materials for course")


class MaterialsByCourseVars(Resource):
    def get(self, term_name, dept_code, course_code, section_code):
        try:
            adoption = Adoptions.select(Adoptions.magento_course) \
                .join(Departments, JOIN_LEFT_OUTER) \
                .switch(Adoptions).join(TermNames, JOIN_LEFT_OUTER, on=(Adoptions.term_name == TermNames.id)) \
                .where(TermNames.term_name == term_name) \
                .where(Departments.department_code == dept_code) \
                .where(Adoptions.course_code == course_code) \
                .where(Adoptions.section_code == section_code) \
                .get()

        except:
            return abort(400, message="No such course")

        try:
            return jsonify({"materials": get_materials(adoption.magento_course)})

        except:
            return abort(400, message="No materials for course")


# API resource routing
api_base_url = "/api"
api.add_resource(Terms, api_base_url + "/v1/terms")
api.add_resource(Term, api_base_url + "/v1/term/<int:term_id>")
api.add_resource(DeptsByTerm, api_base_url + "/v1/departments_by_term/<int:term_id>")
api.add_resource(CoursesByDept, api_base_url + "/v1/courses_by_dept/<int:department_id>")
api.add_resource(CoursesByTerm, api_base_url + "/v1/courses_by_term/<int:term_id>")
api.add_resource(SectionsByCourse, api_base_url + "/v1/sections_by_course/<int:department_id>/<string:course_code>")
api.add_resource(MaterialsByCourseID, api_base_url + "/v1/materials_by_id/<int:course_id>")
api.add_resource(MaterialsByCourseVars, api_base_url + "/v1/materials/<string:term_name>/<string:dept_code>/<string:course_code>/<string:section_code>")


if __name__ == '__main__':
    app.run(debug=True)
