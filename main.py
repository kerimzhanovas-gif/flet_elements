import flet as ft
from app import ProfileApp

def main(page: ft.Page):
    ProfileApp(page)

ft.app(target=main)