from django.contrib import admin

from app.models import MyModel, RelatedModel

# Register your models here.

admin.site.site_header = 'Your Custom Site Header' # заголовок для адміністративної панелі 
admin.site.site_title = 'Your Custom Site Title' # Встановлюється назва сайту

# Кастомізація списку моделей
@admin.register(MyModel) # реєструє модель MyModel у адміністративному інтерфейсі.
class MyModelAdmin(admin.ModelAdmin): # admin.ModelAdmin, що дозволяє налаштувати відображення моделі у адміністративному інтерфейсі.
    list_display = ('field1', 'field2', 'field3') # визначає список полів моделі, які будуть відображені у списку об'єктів моделі.
    list_filter = ('field1',) # дозволяє фільтрувати об'єкти моделі за значенням певного поля.
    search_fields = ('field2',) # визначає поля моделі, за якими можна здійснювати пошук об'єктів.

    # Налаштування редагування багатьох об'єктів одночасно
    actions_on_bottom = True # вказує, що дії (actions) для масової редагування будуть розміщені унизу сторінки.
    actions_on_top = False # вказує, що дії (actions) для масової редагування будуть розміщені унизу сторінки.
    list_per_page = 50 # визначає кількість об'єктів моделі, які будуть відображатись на одній сторінці списку.

    
# Використання fieldsets для групування полів:
@admin.register(RelatedModel)
class MyModelAdmin(admin.ModelAdmin):
    fieldsets = ( # визначає групи полів моделі, що будуть відображатись при редагуванні об'єктів.Кожна група представлена кортежем, що складається з назви групи та словника параметрів. 
        ('General Information', {
            'fields': ('field1', 'field2', 'field3')
        }),
        ('Advanced Options', {
            'classes': ('collapse',), # Параметр classes зі значенням ('collapse',) додає можливість згортання групи полів.
            'fields': ('field4', 'field5'),
        }),
    )