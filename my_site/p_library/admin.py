from django.contrib import admin
from p_library.models import Book, Author, Publisher, Friend, BorrowBook

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
        
    list_display = ('title','author_full_name')
    fields = ('ISBN','title','description','year_release','author', 'publisher','price')
    


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone')
    fields = ('full_name','phone','rating')

@admin.register(BorrowBook)
class BorrowBookAdmin(admin.ModelAdmin):
    pass