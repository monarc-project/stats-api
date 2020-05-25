from flask_mongorest.views import ResourceView
from flask_mongorest.resources import Resource
from flask_mongorest import methods

from statsservice.bootstrap import api
from statsservice.documents.organization import Organization
from statsservice.api.v2.stats import StatsResource


class OrganizationResource(Resource):
    document = Organization
    related_resources = {"stats": StatsResource}
    fields = ["name"]


@api.register(name="organizations", url="organizations/")
class OrganizationsView(ResourceView):
    resource = OrganizationResource
    methods = [
        methods.Create,
        methods.Update,
        methods.Fetch,
        methods.List,
    ]


# The following is a test
# @api.register(name="organization", url="organization/")
# class OrganizationView(ResourceView):
#     resource = OrganizationResource
#     methods = [
#         methods.Delete,
#     ]