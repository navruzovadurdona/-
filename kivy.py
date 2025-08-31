from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Салам, дүйнө!", font_size=32)
        btn = Button(text="Бас!", font_size=24)

        btn.bind(on_press=self.on_button_press)

        layout.add_widget(self.label)
        layout.add_widget(btn)

        return layout

    def on_button_press(self, instance):
        self.label.text = "Баткенден салам 👋"


if __name__ == "__main__":
    MyApp().run()
