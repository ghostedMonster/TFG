from kivy.app import App
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.settings import SettingsWithSidebar

from setttingsjson import settings_json

Builder.load_string('''
<Interface>:
    orientation: 'vertical'
    Button:
        text: 'open the settings!'
        font_size: 150
        on_release: app.open_settings()
''')

class Interface(BoxLayout):
    pass

class SettingsApp(App):
    def build(self):
        self.settings_cls = SettingsWithSidebar
        #con esto podemos guardar el valor de las configuraciones que se ponen,
        # y con eso podemos hacer cosas con los valores puestos
        setting = self.config.get('example', 'boolexample')
        #Con esto, no aparecen los settings de kivy
        self.use_kivy_settings = False
        return Interface()

    def build_config(self, config):
        config.setdefaults('example', {'boolexample': True, 'numericexample': 10,
                                       'optionexample': 'option2',
                                       'stringexample': 'some string',
                                       'pathexample': '/some/path/'})

    def build_settings(self, settings):
        settings.add_json_panel('Panel Name',
                                self.config,
                                data=settings_json)

    def on_config_change(self, config, section, key, value):
        print(config, section, key, value)

SettingsApp().run()