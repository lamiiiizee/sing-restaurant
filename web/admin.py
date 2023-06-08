from django.contrib import admin
from django import forms
# Register your models here.

from . models import Menu
from . models import Branch
from . models import Review
from . models import Contact
from . models import Gallery
from . models import CarouselSlide



admin.site.register(Menu)




class BranchAdminForm(forms.ModelForm):
    branch_contact_number_1 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '+91 0000 0000'}))
    branch_contact_number_2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '+91 0000 0000'}))

    def clean_branch_contact_number_2(self):
        branch_contact_number_2 = self.cleaned_data.get('branch_contact_number_2')
        if branch_contact_number_2.strip() == '':
            return None
        return branch_contact_number_2

    class Meta:
        model = Branch
        fields = '__all__'

class BranchAdmin(admin.ModelAdmin):
    form = BranchAdminForm

admin.site.register(Branch, BranchAdmin)





admin.site.register(Review)
admin.site.register(Contact)
admin.site.register(Gallery)
class CarouselSlideAdmin(admin.ModelAdmin):
    exclude = ('prev_slide',)

admin.site.register(CarouselSlide, CarouselSlideAdmin)


