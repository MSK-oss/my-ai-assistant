from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform

class PersonalAIAgent(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.status_label = Label(text="Private AI Brain: Online\nWaiting for voice command...", halign="center", font_size='20sp')
        layout.add_widget(self.status_label)
        self.talk_btn = Button(text="Tap to Speak", size_hint=(1, 0.3), background_color=(0.1, 0.6, 0.8, 1))
        layout.add_widget(self.talk_btn)
        
        if platform == 'android':
            from android import start_service
            start_service(title="AI Brain", description="Processing context...", arg="")
            
        return layout

if __name__ == '__main__':
    PersonalAIAgent().run()
