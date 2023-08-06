from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QApplication, QComboBox, QGridLayout
from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QGraphicsRectItem
from PySide2.QtGui import QPixmap, QBrush, QColor
from PySide2.QtCore import Qt
from urllib.request import urlopen

class SimGraphicsView(QGraphicsView):
  def __init__(self, scene, key_handler):
      super().__init__(scene)
      self.key_handler=key_handler
  def keyPressEvent(self, event):
    self.key_handler(event)

class SimGuiApp(QApplication):
    SCENE_WIDTH=400
    SCENE_HEIGHT=300
    def __init__(self) -> None:
        super().__init__()
        self.mod=None
    def start(self, mod):
        self.mod=mod
        self.key_ev=None
        self.gs=None
        self.gv=None
        self.gi_dict={}
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
        lbl=QLabel(str(text))
        self.add_wid(name, lbl, **kwargs)
    def add_button(self, name, text, **kwargs):
        btn=QPushButton(text)
        def on_click():
          self.call_handler("on_click_"+name)
        btn.clicked.connect(on_click)
        self.add_wid(name, btn, **kwargs)
    def set_label_text(self, name, text):
      self.get_wid(name).setText(str(text))
    def set_wid_max_size(self, name, w, h):
      wid=self.get_wid(name)
      wid.setMaximumSize(w, h)
    def set_wid_color(self, name, color):
      wid=self.get_wid(name)
      wid.setStyleSheet(f"background-color: {color}")
    def set_label_img(self, name, img_url):
      data=urlopen(img_url).read()
      pm=QPixmap()
      pm.loadFromData(data)
      lbl=self.get_wid(name)
      lbl.setScaledContents(True)
      lbl.setPixmap(pm)
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
        cb.addItem(str(item))
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
    def add_graphics_view(self, min_w, min_h):
        if self.gs:
          raise ValueError("Only one graphics view can be added")
        def on_key(event):
          self.key_ev=event
          self.call_handler("on_key")
        self.gs=QGraphicsScene()
        self.gv=SimGraphicsView(self.gs, on_key)
        self.gv.setMinimumSize(min_w, min_h)
        self.gv.setSceneRect(0, 0, SimGuiApp.SCENE_WIDTH, SimGuiApp.SCENE_HEIGHT)
        self.add_wid("simgui_gv", self.gv)
    def add_gi_img(self, name, x, y, w, h, img_url):
      data=urlopen(img_url).read()
      pm=QPixmap()
      pm.loadFromData(data)
      pm2=pm.scaled(w, h, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
      gi=QGraphicsPixmapItem(pm2)
      gi.setPos(x, y)
      self.add_gi(name, gi)
    def add_gi_rect(self, name, x, y, w, h, color):
      gi=QGraphicsRectItem(x, y, w, h)
      br=QBrush(QColor(color))
      gi.setBrush(br)
      self.add_gi(name, gi)
    def add_gi(self, name, gi):
      if self.gs==None:
        raise ValueError("Must add a graphics scene first")
      if name in self.gi_dict:
        raise ValueError(f"Graphics item {name} already exists")
      self.gi_dict[name]=gi
      self.gs.addItem(gi)
    def get_key(self):
      code_map={Qt.Key_Left: "Left", Qt.Key_Right: "Right", Qt.Key_Up: "Up", Qt.Key_Down: "Down", \
            Qt.Key_Enter: "Enter", Qt.Key_Insert: "Insert", Qt.Key_Delete: "Delete", \
            Qt.Key_Return: "Enter", Qt.Key_Home: "Home", Qt.Key_End: "End",
            Qt.Key_PageUp: "PageUp", Qt.Key_PageDown: "PageDown" }
      key=self.key_ev.key()
      txt=self.key_ev.text()
      if key in code_map:
        return code_map[key]
      elif txt:
        return txt
      else:
        return "Unknown"

sgapp=SimGuiApp()

def start(mod):
    sgapp.start(mod)

def add_label(name, text, **kwargs):
    sgapp.add_label(name, text, **kwargs)

def set_label_text(name, text):
    sgapp.set_label_text(name, text)

def set_label_img(name, img_url):
    sgapp.set_label_img(name, img_url)

def set_wid_color(name, color):
    sgapp.set_wid_color(name, color)

def set_wid_max_size(name, w, h):
    sgapp.set_wid_max_size(name, w, h)

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

def add_graphics_view(min_w, min_h):
  sgapp.add_graphics_view(min_w, min_h)

def add_gi_img(name, x, y, w, h, img_url):
  sgapp.add_gi_img(name, x, y, w, h, img_url)

def add_gi_rect(name, x, y, w, h, color):
  sgapp.add_gi_rect(name, x, y, w, h, color)

def get_key():
  return sgapp.get_key()