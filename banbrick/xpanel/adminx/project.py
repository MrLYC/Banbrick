from core import models
import xadmin


class ProjectAdmin(object):
    list_display = (
        'id', 'name', 'status', 'created_on', 'updated_on',
        'description', 'group', 'tag_set',
    )
    search_fields = (
        'name', 'description',
    )
    list_filter = (
        'status', 'created_on', 'updated_on',
        'group', 'tag_set',
    )
    list_display_links = (
        'id', 'name',
    )

    def get_list_queryset(self):
        qs = super(ProjectAdmin, self).get_list_queryset()
        user = self.request.user
        if user.is_superuser:
            return qs
        return qs.filter(group__in=user.groups.all())

xadmin.site.register(models.Project, ProjectAdmin)
