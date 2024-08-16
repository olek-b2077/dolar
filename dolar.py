from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
app=QApplication([])
win=QWidget()


win.setWindowTitle("0_0")
win.resize(500,300)

enter_dolars = QLineEdit()
#enter_pasvord = QLineEdit()

enter_dolars.setPlaceholderText("dolar")

#enter_pasvord.setPlaceholderText("pasvord")

login_buton = QPushButton("в гривнях")

rov=QHBoxLayout()

col=QVBoxLayout()

rov.addWidget(enter_dolars)
#rov.addWidget(enter_pasvord)

col.addLayout(rov)
col.addWidget(login_buton)

win.setLayout(col)

valut_dolars_in_uah=42,23

def in_grivna(dolars):
    try:
        dolars_ = int( dolars.text)
    except:
        mw_s=QMessageBox()
        mw_s.setText("Enter num")
        mw_s.show()
        mw_s.exec_()
    uah_sum = dolars_ * valut_dolars_in_uah
    mw_s=QMessageBox()
    mw_s.setText(uah_sum ,"грн")
    mw_s.show()
    mw_s.exec_()

login_buton.clicked.connect(in_grivna(enter_dolars))



win.show()
app.exec_()














# def chake_edit():
#     pasvord = enter_pasvord.text()
#     if len(pasvord) < 6:
#         mw_s=QMessageBox()
#         mw_s.setText("pleas enter login")
#         print(pasvord)
#         mw_s.show()
#         mw_s.exec_()
#     else:
#         mw_s=QMessageBox()
#         mw_s.setText("password corekt")
#         mw_s.show()
#         mw_s.exec_()
    
# login_buton.clicked.connect(chake_edit)