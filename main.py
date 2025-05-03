from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget
,QHBoxLayout , QVBoxLayout, QGroupBox, QRadioButton , 
QPushButton,QLabel)
from random import shuffle 

App = QApplication([])
btn_OK = QPushButton('Answer')
lb_Question = QLabel('The most difficult question in the world!')


RadioGroupBox = GroupBox('Answer options')
rbtn_1= QRadioButton("option 1")
rbtn_2= QRadioButton("option 2")
rbtn_3= QRadioButton("option 3")
rbtn_4= QRadioButton("option 4")

RdioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 =  QHBoxLayout()
layout_ans2 =  QVBoxLayout()
layout_ans3 =  QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3)

RadioGroupBox.setLayout(Layout_ans1)

AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('are you correct or no')
lb_Correct = QLabel('the answer will be here!')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alghnment = Qt.AlignHCenter, stretch = 2 )
AnsGroupBox.setLayout(Layout_res)



layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_Question, alignment-(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.SetSpacing(5)

def ask (question, right_answer, wrong1 , wrong2 , wrong3):
     shuffle(answers)
     answers[0].setText(right_answer)
     answers[1].setText(wrong1)
     answers[2].setText(wrong2)
     answers[3].setText(wrong3)
     lb_question.setText(question)
     lb_correct.setText(right_answer)
     show_question()

def show_question():
    radioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')
    RadioGroup.SetExclusive(False)
    rbtn_1.SetChecked(False)
    rbtn_2.SetChecked(False)
    rbtn_3.SetChecked(False)
    rbtn_4.SetChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')

answers= [rbtn_1, rbtn_2 , rbtn_3 , rbtn_4]

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('Correct!')
    else:

        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_incorrect('Incorrect!')
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo card')            
ask("The national language of Brazil","portuguese","Brazilian", "spanish", "Italian")
btn_OK.clicked.connect(check_answer)



window.SetLayout(layout_card)
window.show()
app.exec()















