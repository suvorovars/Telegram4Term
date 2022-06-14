import npyscreen

from form.Boxes import InputMessBox, ChatBox, InputSearchBox, ListChatBox


class MainForm(npyscreen.ActionForm):
    # Конструктор
    def create(self):
        # Добавляем виджет TitleText на форму
        y, x = self.useable_space()
        self.add(InputMessBox, name='Ввод:', relx= x // 4, rely= y - y // 5)
        self.add(ListChatBox, name='Чаты:', relx=2, rely=2,  max_width=x // 4 - 2)
        self.add(ChatBox, name='Сообщения', relx=x // 4, rely=2, max_height=y - y // 5 - 2)
    # переопределенный метод, срабатывающий при нажатии на кнопку «ok»
    def on_ok(self):
        self.parentApp.setNextForm(None)
    # переопределенный метод, срабатывающий при нажатии на кнопку «cancel»
    def on_cancel(self):
        self.title.value = "Hello World!"