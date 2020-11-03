from django.contrib import admin
from testapp.models import monday_model1,column_model1
# Register your models here.
class monday_admin1(admin.ModelAdmin):
    list=['day','firstperiod','secondperiod','thirdperiod','fourthperiod','fifthperiod','sixthperiod','seventhperiod','eightperiod']

class column_admin1(admin.ModelAdmin):
    list=['periodno','monday','tuesday','wednesday','thrusday','friday','saturday']

admin.site.register(monday_model1,monday_admin1)
admin.site.register(column_model1,column_admin1)
