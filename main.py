from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MonAppSimple(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(
            text="Bienvenue sur mon application !", 
            font_size='20sp'
        )
        
        bouton = Button(
            text="Cliquez-moi !", 
            size_hint=(1, 0.3),
            background_color=(0.1, 0.6, 0.8, 1)
        )
        bouton.bind(on_press=self.action_bouton)
        
        layout.add_widget(self.label)
        layout.add_widget(bouton)
        
        return layout

    def action_bouton(self, instance):
        self.label.text = "Bravo ! L'application fonctionne sur votre Redmi 12."

if __name__ == '__main__':
    MonAppSimple().run()
