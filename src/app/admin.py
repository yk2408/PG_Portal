from django.contrib import admin
from .models import Booking, Contact_us, Review, FacilitiesPrice, CheckAvailibility, Owner, Payment, Photo
# Register your models here.


class AvailibilityAdmin(admin.ModelAdmin):
	list_display = [
			'name',
			'pg_type',
			'available_from',
			'available_to',
			'no_of_person',
			'area',
			'available'
	]
	list_filter = ['pg_type', 'available_from', 'available_to', 'area', 'no_of_person']


class FacilityAdmin(admin.ModelAdmin):
	list_display = [
			'name',
			'price'
	]

class BookingAdmin(admin.ModelAdmin):
	list_display = [
			'fname',
			'lname',
			'arrival_date',
			'departure_date',
			'gender',
			'sharing',
			'wifi',
            'loundry',
            'maid',
            'food'
	]
	list_filter = ['gender', 'arrival_date', 'departure_date']
	search_fields = ['gender']

	class Meta:
		model = Booking

class ContactAdmin(admin.ModelAdmin):
	list_display = [
			'fname',
			'lname',
			'email',
			'contact',
			'message'
	]
	search_fields = ['fname', 'contact']

class ReviewAdmin(admin.ModelAdmin):
	list_display = [
			'fname',
			'lname',
			'email',
			'pg_type',
			'comfort',
			'cost',
			'quality'
	]
	search_fields = ['confort','cost', 'quality', 'pg_type']
	list_filter = ['email', 'cost', 'quality', 'pg_type']

class PhotoAdmin(admin.TabularInline):
	model = Photo
	max_num = 10

class OwnerAdmin(admin.ModelAdmin):
	list_display = [
			'name',
			'contact',
			'email',
			'pg_type',
			'description',
			'price',
			'sharing',
			'wifi',
			'loundry',
			'food',
			'maid',
	]
	inlines = [
			PhotoAdmin
	]
	search_fields = ['pg_type']

class PaymentAdmin(admin.ModelAdmin):
	list_display = [
			'ac_no',
			'ini_balance',
			'rem_balance'
	]

admin.site.register(Booking, BookingAdmin)
admin.site.register(Contact_us, ContactAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(FacilitiesPrice, FacilityAdmin)
admin.site.register(CheckAvailibility, AvailibilityAdmin)
admin.site.register(Photo)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Payment, PaymentAdmin)
# admin.site.register(ActivationProfile)
admin.site.site_title = "PG Portal"
admin.site.site_header = "PG Portal"
