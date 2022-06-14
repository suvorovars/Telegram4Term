import npyscreen


class InputMessBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

class InputSearchBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

class ChatBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

class ListChatBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit