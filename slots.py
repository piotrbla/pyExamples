from qtpy.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
import time


class DamTerm(QObject): #Main Class
    def __init__(self, addr):
        super(self.__class__, self).__init__()
        self.start()

    @pyqtSlot(str)
    def take_info(self, _str):
        print("TAKE::INFO:: %s" % _str)
        with open("test", "w") as f:
            f.write("Test")
        self.info.write(_str)

    def test(self):
        print("TESTETT!")


    def start(self):
        print("Start!")
        self.GenUids = GenerateUids(self)
        self.th = QThread(self)
        self.th.setObjectName("GenerateUids")
        self.GenUids.moveToThread(self.th)
        self.GenUids.pasInfo.connect(self.take_info)
        self.th.started.connect(self.GenUids.run)
        self.th.start()
        while not self.th.isFinished():
            time.sleep(1)
            print("while")
        print("Koniec startu")


class GenerateUids(QObject):  #MyWorker
    pasInfo = pyqtSignal(str)
    testt = pyqtSignal()

    def __init__(self, term):
        super(self.__class__, self).__init__()
        self.term = term

    def run(self):
        #Qthread stuff
        self.testt.emit()
        self.pasInfo.emit("To się nie wyświetla")
        print("To się wyświetla")
        self.term.test()  #to też się wyświetla


if __name__ == "__main__":
    import sys
    d = DamTerm(addr=5)