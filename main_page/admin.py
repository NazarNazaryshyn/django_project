from django.contrib import admin
from .models import Category, Dish, Advantage, Chef, Gallery, Slide, Customer, Photo, UserReservation, UserContacts




class ChefAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('second_name',)}

admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Advantage)
admin.site.register(Chef, ChefAdmin)
admin.site.register(Gallery)
admin.site.register(Slide)
admin.site.register(Customer)
admin.site.register(Photo)
admin.site.register(UserReservation)
admin.site.register(UserContacts)



