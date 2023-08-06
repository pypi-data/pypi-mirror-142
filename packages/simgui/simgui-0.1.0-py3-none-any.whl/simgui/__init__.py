from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QApplication, QComboBox, QGridLayout

class SimGuiApp(QApplication):
    def __init__(self) -> None:
        super().__init__()
        self.mod=None
    def start(self, mod):
        self.mod=mod
        self.wid_dict={}
        self.last_row=None
        self.auto_row=0
        self.auto_col=0
        wid=QWidget()
        wid.setWindowTitle("simgui")
        self.lo=QGridLayout()
        wid.setLayout(self.lo)
        self.call_handler("on_ready")
        wid.show()
        self.exec_()
    def call_handler(self, fn):
        handler=self.mod.get(fn)
        if handler:
          handler()
    def add_label(self, name, text, **kwargs):
        lbl=QLabel(text)
        self.add_wid(name, lbl, **kwargs)
    def add_button(self, name, text, **kwargs):
        btn=QPushButton(text)
        def on_click():
          self.call_handler("on_click_"+name)
        btn.clicked.connect(on_click)
        self.add_wid(name, btn, **kwargs)
    def set_label_text(self, name, text):
      self.get_wid(name).setText(str(text))
    def add_wid(self, name, w, **kwargs):
      if not (name in self.wid_dict):
        self.wid_dict[name]=w
        if "right" in kwargs:
          row=self.last_row
          col=self.auto_col
        else:
          row=self.auto_row
          col=0
        row=kwargs.get("row", row)
        col=kwargs.get("col", col)
        rows=kwargs.get("rows", 1)
        cols=kwargs.get("cols", 1)
        self.lo.addWidget(w, row, col, rows, cols)
        self.last_row=row
        self.auto_row=row+rows
        self.auto_col=col+cols
      else:
        raise ValueError(f"widget named {name} already exists", name)
    def get_wid(self, name):
      if name in self.wid_dict:
        return self.wid_dict[name]
      else:
        raise ValueError(f"no widget named {name}", name)
    def add_input(self, name, **kwargs):
        edit=QLineEdit()
        def on_edited():
          self.call_handler("on_edited_"+name)
        edit.textEdited.connect(on_edited)
        self.add_wid(name, edit, **kwargs)
    def add_combo(self, name, **kwargs):
        cb=QComboBox()
        def on_idx_changed():
          self.call_handler("on_index_changed_"+name)
        cb.currentIndexChanged.connect(on_idx_changed)
        self.add_wid(name, cb, **kwargs)
    def add_combo_item(self, name, item):
        cb=self.get_wid(name)
        cb.addItem(item)
    def get_combo_text(self, name):
        cb=self.get_wid(name)
        return cb.currentText()
    def get_input_text(self, name):
      inp=self.get_wid(name)
      return inp.text()
    def get_input_num(self, name):
      t=self.get_input_text(name)
      return int(t)
    def get_input_value(self, name):
      t=self.get_input_text(name)
      try:
        return int(t)
      except:
        return t
    def set_input_text(self, name, text):
      self.get_wid(name).setText(str(text))

sgapp=SimGuiApp()

def start(mod):
    sgapp.start(mod)

def add_label(name, text, **kwargs):
    sgapp.add_label(name, text, **kwargs)

def set_label_text(name, text):
    sgapp.set_label_text(name, text)

def add_button(name, text, **kwargs):
    sgapp.add_button(name, text, **kwargs)    

def add_input(name, **kwargs):
    sgapp.add_input(name, **kwargs)    

def get_input_text(name):
    return sgapp.get_input_text(name)        

def get_input_num(name):
    return sgapp.get_input_num(name)        

def get_input_value(name):
    return sgapp.get_input_value(name)        

def set_input_text(name, text):
    return sgapp.set_input_text(name, text)

def add_combo(name, **kwargs):
  sgapp.add_combo(name, **kwargs)      

def add_combo_item(name, item):
  sgapp.add_combo_item(name, item)

def get_combo_text(name):
  return sgapp.get_combo_text(name)
