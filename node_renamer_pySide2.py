from hutil.Qt.QtWidgets import *

import hou

class myWidget (QWidget):
    def __init__(self):
        super(myWidget, self).__init__()
        self.setProperty("houdiniStyle", True)
        l = QVBoxLayout()

        self.setLayout(l)


# -------------------------------Start GrpBox--------------------------------------
        grpBox = QGroupBox("Enter Your Prefix or Postfix")
        label_name = QLabel("New Name")
        self.line_name = QLineEdit()
        button_print_pref = QPushButton("Print Prefix")
        button_print_post = QPushButton("Print Postfix")


        hbox = QHBoxLayout()
        hbox.addWidget(label_name)
        hbox.addWidget(self.line_name)
        hbox.addWidget(button_print_pref)
        hbox.addWidget(button_print_post)


        grpBox.setLayout(hbox)

        l.addWidget(grpBox)

# -------------------------------end GrpBox--------------------------------------

# -------------------------------Start GrpBox2--------------------------------------
        grpBox2 = QGroupBox("Enter New Node Name")
        label_new_name = QLabel("New Name")
        self.line_new_name = QLineEdit()
        button_clear_name = QPushButton("New Name")


        hbox2 = QHBoxLayout()
        hbox2.addWidget(label_new_name)
        hbox2.addWidget(self.line_new_name)
        hbox2.addWidget(button_clear_name)


        grpBox2.setLayout(hbox2)

        l.addWidget(grpBox2)

# -------------------------------end GrpBox2--------------------------------------

        spacerItem = QSpacerItem(40, 400, QSizePolicy.Expanding, QSizePolicy.Expanding)
        l.addItem(spacerItem)
        button_print_pref.clicked.connect(self.actionPref)
        button_print_post.clicked.connect(self.actionPost)
        button_clear_name.clicked.connect(self.clearPref)

        

    def actionPref(self):
        nodes = hou.selectedNodes()
        for n in nodes:
            if str(self.line_name.text()):
                n.setName(str(self.line_name.text()) + "_" + n.name())

    def actionPost(self):
        nodes = hou.selectedNodes()
        for n in nodes:
            if str(self.line_name.text()):
                n.setName(n.name() + "_" + str(self.line_name.text()))


    def clearPref(self): 
        nodes = hou.selectedNodes()
        for n in nodes:
            if str(self.line_new_name.text()):
                n.setName(str(self.line_new_name.text()), 1)




def createInterface():
    w = myWidget()
    return w
