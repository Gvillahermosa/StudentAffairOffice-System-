from django.contrib import admin
from . models import Studentinfo, CaseProfile, GoodMoral, CommunityServiceTracker
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class StudentResource(resources.ModelResource):
    class Meta:
        model = Studentinfo
        import_id_fields = ['studentID']
        fields = ('studentID', 'lrn', 'lastname', 'firstname', 'middlename', 'degree', 'year_level', 'sex', 'email', 'contact_number')

class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    list_display = ['studentID', 'lrn', 'lastname', 'firstname', 'middlename', 'degree', 'year_level', 'sex', 'email', 'contact_number']

admin.site.register(Studentinfo, StudentAdmin)
admin.site.register(CaseProfile)
admin.site.register(GoodMoral)
admin.site.register(CommunityServiceTracker)