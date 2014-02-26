from django.contrib import admin
from myapp.models import gadb_action, gadb_bill, gadb_legislator, gadb_stats, gadb_vote

# Register your models here.

class gadb_actionAdmin(admin.ModelAdmin):
    search_fields = ('name',),
    
admin.site.register(gadb_action, gadb_actionAdmin)

class gadb_billAdmin(admin.ModelAdmin):
    search_fields = ('name',),
    
admin.site.register(gadb_bill, gadb_billAdmin)

class gadb_legislatorAdmin(admin.ModelAdmin):
    search_fields = ('name',),
    
admin.site.register(gadb_legislator, gadb_legislatorAdmin)

class gadb_statsAdmin(admin.ModelAdmin):
    search_fields = ('name',),
    
admin.site.register(gadb_stats, gadb_statsAdmin)

class gadb_voteAdmin(admin.ModelAdmin):
    search_fields = ('name',),
    
admin.site.register(gadb_vote, gadb_voteAdmin)