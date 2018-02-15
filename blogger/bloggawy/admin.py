from django.contrib import admin
from .models import Track,Student

class CustomPost(admin.ModelAdmin):
	fieldsets=(
		['Post_Info',{'fields':['time','text']}])
	list_display=('time','text')
	list_filter=['time']

class CustomCategories(admin.ModelAdmin):
	fieldsets=(
		['Category_Info',{'fields':['name']}])
	list_display=('name')
	list_filter=['name']
class CustomCurses(admin.ModelAdmin):
	fieldsets=(
		['Curse_Info',{'fields':['text','replacment']}])
	list_display=('text')
	list_filter=['text']
	# search_fields=['track__track_name']

# class InlineStudent(admin.StackedInline):
# 	model=Student
# 	extra=4
# class CustomTrack(admin.ModelAdmin):
# 	inlines=[InlineStudent]
# admin.site.register(Track,CustomTrack)
# admin.site.register(Student,CustomStudent)