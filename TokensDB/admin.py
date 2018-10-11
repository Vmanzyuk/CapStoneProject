from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect


from .models import Token, Token_price
from .utils import fill_main_info, fill_additional_info

class MyModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('deletealltokens/', self.admin_site.admin_view(self.delete_all_tokens)),
            path('firstfill/', self.admin_site.admin_view(self.first_fill))
        ]
        return my_urls + urls

    def delete_all_tokens(self, request):
        self.model.objects.all().delete()
        self.message_user(request, "All tokens was deleted")
        return HttpResponseRedirect("../")

    def first_fill(self, request):
        fill_main_info()
        fill_additional_info()
        self.message_user(request, "Sucessful first fill")
        return HttpResponseRedirect("../")




class TokenAdmin(MyModelAdmin):
    list_display = ('id','name','symbol','explorer','based_on_blockchain','smart_contract_address')
    change_list_template = "entities/tokens_changelist.html"

admin.site.register(Token,TokenAdmin)
admin.site.register(Token_price)
# Register your models here.
