import flet as ft
from ui import UI
from email_service import EmailService

class ProfileApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = 'Анкеты'
        self.page.window_width = 550
        self.page.window_height = 700
        self.page.theme_mode = ft.ThemeMode.LIGHT

        self.ui = UI()
        self.email_service = EmailService()

        self.page.overlay.append(self.ui.photo_picker)
        self.page.add(*self.ui.build())
        self.build_event()
    
    def build_event(self):
        self.ui.button.on_click = self.create_profile
        self.ui.age.on_change = self.update_age
    
    def update_age(self, e):
        self.ui.age_text.value = f'Возраст: {int(self.ui.age.value)}'
        self.page.update()
    
    def validate_fields(self):
        errors = []
        
        if not self.ui.name.value or not self.ui.name.value.strip():
            self.ui.name.error_text = "Имя обязательно для заполнения"
            errors.append("Имя не заполнено")
        else:
            self.ui.name.error_text = None
        
        if not self.ui.city.value:
            self.ui.city.error_text = "Выберите город"
            errors.append("Город не выбран")
        else:
            self.ui.city.error_text = None
        
        self.page.update()
        return len(errors) == 0
    
    def create_profile(self, e):
        if not self.validate_fields():
            self.ui.error_message.value = "❌ Пожалуйста, заполните обязательные поля (отмечены *)"
            self.page.update()
            return
        
        skills = []
        if self.ui.skill1.value:
            skills.append("Python")
        if self.ui.skill2.value:
            skills.append("Django")
        if self.ui.skill3.value:
            skills.append("Flet")
        
        level_value = self.ui.level.value if self.ui.level.value else "Не указан"
        
        profile_data = {
            'name': self.ui.name.value,
            'city': self.ui.city.value,
            'age': int(self.ui.age.value),
            'skills': skills,
            'level': level_value,
            'ready': "Да" if self.ui.active.value else "Нет"
        }
        
        skills_text = ", ".join(skills) if skills else "Не указаны"
        
        self.ui.result.value = (
            f'✅ Анкета создана!\n\n'
            f'Имя: {profile_data["name"]}\n'
            f'Город: {profile_data["city"]}\n'
            f'Возраст: {profile_data["age"]}\n'
            f'Навыки: {skills_text}\n'
            f'Уровень: {profile_data["level"]}\n'
            f'Готов к работе: {profile_data["ready"]}'
        )
        
        success, message = self.email_service.send_notification({
            'name': profile_data['name'],
            'city': profile_data['city'],
            'age': profile_data['age'],
            'skills': skills_text,
            'level': profile_data['level'],
            'ready': profile_data['ready']
        })
        
        if success:
            self.ui.error_message.value = f"📧 {message}"
            self.ui.error_message.color = "green"
        else:
            self.ui.error_message.value = f"⚠️ Анкета создана, но {message}"
            self.ui.error_message.color = "orange"
        
        self.clear_form()
        self.page.update()
    
    def clear_form(self):
        self.ui.name.value = ""
        self.ui.city.value = None
        self.ui.age.value = 10
        self.ui.age_text.value = "Возраст: 10"
        self.ui.skill1.value = False
        self.ui.skill2.value = False
        self.ui.skill3.value = False
        self.ui.level.value = None
        self.ui.active.value = False
        self.ui.photo_preview.src = ""
        self.ui.photo_path.value = ""