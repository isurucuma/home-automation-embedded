from PySide6.QtWidgets import QApplication, QMainWindow
import boardSerial


import output_new as output

class MainWindow(QMainWindow, output.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.tempLabel.setText("temp altered")
        self.humidLabel.setText("humid altered")



app = QApplication([])
    # Create and show the application's main window
win = MainWindow()

win.tempOnLbl.setText("12°C")
win.tempOffLbl.setText("12°C")


# create a thread to update the labels
from threading import Thread
import time




# there should be a loop which sends commands to the board for every 2 seconds
special_commands = []
stopLoop  = False
def sendCommandsLoop():
    ticks = 0
    command_to_send = ""
    while(True):
        if special_commands == []:
            if ticks == 0:
                command_to_send = "%a%\n"
                boardSerial.sendCommend(command_to_send)
                time.sleep(2.2)
                data = boardSerial.readData()
                ticks = 5
                
                if data != "":
                    (humid, temp) = boardSerial.filterData(data)
                    win.tempLabel.setText(temp)
                    win.humidLabel.setText(humid)

                continue
            ticks -= 1
            time.sleep(0.2)
            

        else: # if there are special commands to send
            command_to_send = special_commands.pop(0)
            time.sleep(0.5)
            boardSerial.sendCommend(command_to_send)
            time.sleep(1)

        print(special_commands)

        if stopLoop:
            break

# create a thread to run the sendCommandsLoop
sendCommandsThread = Thread(target=sendCommandsLoop)
sendCommandsThread.start()


def btnClicked(btn, btnNum):
    if btn.isChecked():
        special_commands.append(f"%bsw{btnNum}1%\n")
    else:
        special_commands.append(f"%bsw{btnNum}0%\n")

def formatTime(hour, minute):
    if hour < 10:
        hour = f"0{hour}"
    if minute < 10:
        minute = f"0{minute}"
    return hour, minute

def timerbtnClicked(btn, btnNum):
    if btnNum == 1:
        on_hour = win.timeEdit_11.time().hour()
        on_minute = win.timeEdit_11.time().minute()

        on_hour, on_minute = formatTime(on_hour, on_minute)

        off_hour = win.timeEdit_12.time().hour()
        off_minute = win.timeEdit_12.time().minute()

        off_hour, off_minute = formatTime(off_hour, off_minute)

        #%esw1h02m30#h02m30%
        special_commands.append(f"%esw1h{on_hour}m{on_minute}#h{off_hour}m{off_minute}%\n")
    
    elif btnNum == 2:
        on_hour = win.timeEdit_21.time().hour()
        on_minute = win.timeEdit_21.time().minute()

        on_hour, on_minute = formatTime(on_hour, on_minute)

        off_hour = win.timeEdit_22.time().hour()
        off_minute = win.timeEdit_22.time().minute()

        off_hour, off_minute = formatTime(off_hour, off_minute)

        #%esw2h02m30#h02m30%
        special_commands.append(f"%esw2h{on_hour}m{on_minute}#h{off_hour}m{off_minute}%\n")

    elif btnNum == 3:
        on_hour = win.timeEdit_31.time().hour()
        on_minute = win.timeEdit_31.time().minute()

        on_hour, on_minute = formatTime(on_hour, on_minute)

        off_hour = win.timeEdit_32.time().hour()
        off_minute = win.timeEdit_32.time().minute()

        off_hour, off_minute = formatTime(off_hour, off_minute)

        #%esw3h02m30#h02m30%
        special_commands.append(f"%esw3h{on_hour}m{on_minute}#h{off_hour}m{off_minute}%\n")

def tempSetBtnClicked(btn, btnNum): #%csw1tmp30#tmp20%
    tempOn = str(win.tempOnDial.value())
    tempOff = str(win.tempOffDial.value())

    if btnNum == 1:        
        special_commands.append(f"%csw1tmp{tempOn}#tmp{tempOff}%\n")

    elif btnNum == 2:
        special_commands.append(f"%csw2tmp{tempOn}#tmp{tempOff}%\n")

    elif btnNum == 3:
        special_commands.append(f"%csw3tmp{tempOn}#tmp{tempOff}%\n")

    win.tempOnDial.setValue(0)
    win.tempOffDial.setValue(0)


# attaching button events
win.lightsBtn1.clicked.connect(lambda: btnClicked(win.lightsBtn1, 1))
win.lightsBtn2.clicked.connect(lambda: btnClicked(win.lightsBtn2, 2))
win.lightsBtn3.clicked.connect(lambda: btnClicked(win.lightsBtn3, 3))

# attaching timer btn events
win.timerBtn1.clicked.connect(lambda: timerbtnClicked(win.timerBtn1, 1))
win.timerBtn2.clicked.connect(lambda: timerbtnClicked(win.timerBtn2, 2))
win.timerBtn3.clicked.connect(lambda: timerbtnClicked(win.timerBtn3, 3))

# attaching temp Dial value change events
win.tempOnDial.valueChanged.connect(lambda: win.tempOnLbl.setText(str(round(win.tempOnDial.value())) + "°C"))
win.tempOffDial.valueChanged.connect(lambda: win.tempOffLbl.setText(str(round(win.tempOffDial.value())) + "°C"))

# attaching temp set btn events
win.tempSetBtn1.clicked.connect(lambda: tempSetBtnClicked(win.tempSetBtn1, 1))
win.tempSetBtn2.clicked.connect(lambda: tempSetBtnClicked(win.tempSetBtn2, 2))
win.tempSetBtn3.clicked.connect(lambda: tempSetBtnClicked(win.tempSetBtn3, 3))



win.show()
app.exec()

stopLoop = True
# loopthread.join()
sendCommandsThread.join()
print("All processes finished...")

