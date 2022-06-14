import npyscreen

from form.TgForm import MainForm


class App(npyscreen.StandardApp):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        self.addForm("MAIN", MainForm, name="Telegram4Term")

MyApp = App()
MyApp.run()