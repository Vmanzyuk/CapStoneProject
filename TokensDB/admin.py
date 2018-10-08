from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect

from .models import Token


class MyModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('deletealltokens/', self.admin_site.admin_view(self.delete_all_tokens)),
            path('firstfill/', self.admin_site.admin_view(self.first_fill))
        ]
        return my_urls + urls

    def delete_all_tokens(self, request):
        self.model.objects.all().update(name='delete')
        self.message_user(request, "All tokens was deleted")
        return HttpResponseRedirect("../")

    def first_fill(self, request):
        self.model.objects.all().update(name='fill')
        self.message_user(request, "Sucessful insert from CMC")
        return HttpResponseRedirect("../")




class TokenAdmin(MyModelAdmin):
	change_list_template="entities/tokens_changelist.html"

admin.site.register(Token,TokenAdmin)

# Register your models here.
