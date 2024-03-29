import xadmin

from myproperty.models import Info, Grant
from import_export import resources
from collections import OrderedDict
from guardian.admin import GuardedModelAdminMixin
from guardian.shortcuts import get_objects_for_user, assign_perm


class MyCourseResource(resources.ModelResource):
    class Meta:
        model = Info


class InfoAdmin(object):
    import_export_args = {"import_resource_class": MyCourseResource, "export_resource_class": MyCourseResource}
    list_display = ['pro_name', 'type', 'sn', 'asset_code', 'current_user', 'requisition_time', 'add_time']
    search_fields = ['pro_name', 'current_user']
    list_filter = ['pro_name', 'current_user', 'requisition_time', 'add_time']
    ordering = ['id']


class GrantAdmin(object):
    list_display = ['device', 'specification', 'user_name', 'info_code', 'alters_date']
    search_fields = ['device', 'user_name', 'alters_date']
    list_filter = ['device', 'user_name', 'alters_date']

    class Meta:
        model = Grant


xadmin.site.register(Info, InfoAdmin)
xadmin.site.register(Grant, GrantAdmin)
