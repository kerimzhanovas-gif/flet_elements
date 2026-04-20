import flet as ft

class UI:
    def __init__(self):
        self.title = ft.Text('Создание пользователей', size=24, weight="bold")
        
        self.name = ft.TextField(
            label='Имя *',
            width=300,
            border_color="blue",
            focused_border_color="blue",
        )
        
        self.city = ft.Dropdown(
            label='Город *',
            width=300,
            options=[
                ft.dropdown.Option('Бишкек'),
                ft.dropdown.Option('Ош'),
                ft.dropdown.Option('Токмок'),
            ],
            border_color="blue",
            focused_border_color="blue",
        )
        
        self.age_text = ft.Text('Возраст: 10', color="blue")
        self.age = ft.Slider(
            min=10,
            max=60,
            divisions=50,
            value=10,
            label="{value}",
            active_color="blue",
        )
        
        self.skill1 = ft.Checkbox(
            label='Python',
            fill_color="blue",
            check_color="white"
        )
        self.skill2 = ft.Checkbox(
            label='Django',
            fill_color="blue",
            check_color="white"
        )
        self.skill3 = ft.Checkbox(
            label='Flet',
            fill_color="blue",
            check_color="white"
        )

        self.level = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value='Jun', label='Junior', fill_color="blue"),
                ft.Radio(value='Mid', label='Middle', fill_color="blue"),
                ft.Radio(value='Sen', label='Senior', fill_color="blue"),
            ])
        )
        
        self.active = ft.Switch(
            label='Готов к работе',
            active_color="blue",
        )

        self.photo_picker = ft.FilePicker()
        self.photo_picker.on_result = self.on_photo_picked
        self.photo_path = ft.Text(color="green")
        self.photo_preview = ft.Image(
            src="",
            width=100,
            height=100,
            fit="cover",
            border_radius=50,
        )
        self.upload_button = ft.ElevatedButton(
            'Загрузить фото',
            on_click=lambda _: self.photo_picker.pick_files(
                allow_multiple=False,
                allowed_extensions=['png', 'jpg', 'jpeg']
            )
        )

        self.button = ft.ElevatedButton(
            'Отправить резюме',
            style=ft.ButtonStyle(
                bgcolor="blue",
                color="white",
            )
        )

        self.result = ft.Text(color="green")
        self.error_message = ft.Text(color="red")
        
    def on_photo_picked(self, e: ft.FilePickerResultEvent):
        if e.files:
            self.photo_path.value = f"Фото выбрано: {e.files[0].name}"
            self.photo_preview.src = e.files[0].path
        else:
            self.photo_path.value = "Фото не выбрано"
        self.photo_path.update()
        self.photo_preview.update()
    
    def build(self):
        return [
            self.title,
            self.name,
            self.city,
            self.age_text,
            self.age,
            ft.Text('Навыки:', weight="bold"),
            self.skill1,
            self.skill2,
            self.skill3,
            ft.Text('Уровень:', weight="bold"),
            self.level,
            self.active,
            ft.Row([
                self.upload_button,
                self.photo_preview,
            ]),
            self.photo_path,
            self.button,
            self.error_message,
            self.result
        ]