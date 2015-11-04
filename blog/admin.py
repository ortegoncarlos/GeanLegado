from django.contrib import admin
from blog.models import Post, Hero, Circles, Featured, Sedes, Slide, Video, Schedule, Speakers, Galeria
from admin_thumbnail import thumb_admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


class SpeakersResourceExcel(resources.ModelResource):
    class Meta:
        model = Speakers

class SpeakersAdmin(admin.ModelAdmin):
    list_display = ('person','awards', )
    list_filter = ('person','awards',)
    list_editable = ('person','awards',)
    search_fields = ('person','awards',)

class SpeakersAdminXls(SpeakersAdmin,ImportExportActionModelAdmin):
    resource_class = SpeakersResourceExcel
    pass

admin.site.register(Speakers,SpeakersAdminXls)

class ScheduleResourceExcel(resources.ModelResource):
    class Meta:
        model = Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title','evento','guests', )
    list_filter = ('title','evento','guests',)
    list_editable = ('title','evento','guests',)
    search_fields = ('title','evento','guests',)

class ScheduleAdminXls(ScheduleAdmin,ImportExportActionModelAdmin):
    resource_class = SpeakersResourceExcel
    pass

admin.site.register(Schedule,ScheduleAdminXls)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'publish', 'created', 'modified')
    list_filter = ('publish',)
    list_editable = ('title',)
    search_fields = ('user__email',)
    prepopulated_fields = {'slug': ['title']}


class PostInline(admin.StackedInline):
    model = Post
    extra = 1



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class AdmissionAdmin(thumb_admin.ThumbAdmin):
    list_display = ('id','title','message','admission_image','timestamp')
    list_editable = ('title','message',)
    search_fields = ('title',)
    list_filter = ('title',)


admin.site.register(Post,PostAdmin)
admin.site.register(Hero)
admin.site.register(Circles)
admin.site.register(Featured)
admin.site.register(Sedes)
admin.site.register(Slide)
admin.site.register(Video)
admin.site.register(Galeria)