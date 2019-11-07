import sys
import os
import configparser
import random
import time

from PyQt5.QtWidgets    import *
from PyQt5.QtGui        import *
from PyQt5.QtCore       import *
from PyQt5.QtMultimedia import *

class MyMusicApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.Play_Pause, self.Preview_Next, self.mp3_url = True, False, ''

    def initUI(self):
        self.SongList = []
        self.player   = QMediaPlayer()

        self.lb1 = QLabel('00:00', alignment=Qt.AlignCenter)
        self.lb2 = QLabel('00:00', alignment=Qt.AlignCenter)
        self.qsl = QSlider(Qt.Horizontal, self)
        self.qsl.sliderMoved[int].connect(self.SetPlayPosition)
        self.btn_play      = QPushButton('Воспроизведение', self, clicked=self.MusicPlay)
        self.btn_preview   = QPushButton('Предыдущая песня', self, clicked=self.MusicPreview)
        self.btn_next      = QPushButton('Следующая песня',self, clicked=self.MusicNext)
        self.btn_openmusic = QPushButton('Выберите папку с музыкой', self, clicked=self.OpenMusic)
        self.lw = QListWidget(itemDoubleClicked=self.MouseDoubleClick)

        if os.path.exists('Setting.ini'):
            config = configparser.ConfigParser()
            config.read("Setting.ini")
            PATH   = config.get('Music', 'PATH')
            self.AddListItems(PATH)
        # Создайте раскрывающийся список, чтобы изменить режим воспроизведения музыки
        self.cmb = QComboBox()
        self.cmb.addItem('Последовательное воспроизведение')
        self.cmb.addItem('Oдин цикл')
        self.cmb.addItem('Случайная игра')

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.PlayMode)
        self.timer.start(1000)

        # Схема сетки
        grid = QGridLayout(self)
        grid.addWidget(self.lw,  0, 0, 1, 0)
        grid.addWidget(self.lb1, 1, 0, 1, 1)
        grid.addWidget(self.qsl, 1, 1, 1, 1)
        grid.addWidget(self.lb2, 1, 2, 1, 1)
        grid.addWidget(self.btn_preview,  2, 0, 1, 1)
        grid.addWidget(self.btn_play,     2, 1, 1, 1)
        grid.addWidget(self.btn_next,     2, 2, 1, 1)
        grid.addWidget(self.cmb,          3, 0, 1, 3)
        grid.addWidget(self.btn_openmusic,4, 0, 1, 3)

    def SetPlayPosition(self):
        self.player.setPosition(self.qsl.value())

    def PlayMode(self):
        if self.Play_Pause==False:
            self.qsl.setMinimum(0)
            self.qsl.setMaximum(self.player.duration())
            self.qsl.setValue(self.qsl.value() + 1000)
        self.lb1.setText(time.strftime('%M:%S',time.localtime(self.player.position()/1000)))
        self.lb2.setText(time.strftime('%M:%S', time.localtime(self.player.duration() / 1000)))

        if self.player.position()==self.player.duration() and self.player.duration()!=0 and self.cmb.currentIndex()==0 and self.Play_Pause==False:
            if self.lw.count() == 0:
                return
            self.MusicNext()
        elif self.player.position()==self.player.duration() and self.player.duration()!=0 and self.cmb.currentIndex()==1 and self.Play_Pause==False:
            if self.lw.count() == 0:
                return
            self.Preview_Next = True
            self.mp3_url = self.SongList[self.lw.currentRow()][1]
            self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
            self.qsl.setValue(0)
            self.MusicPlay()
            self.Preview_Next = False
        elif self.player.position()==self.player.duration() and self.player.duration()!=0 and self.cmb.currentIndex()==2 and self.Play_Pause==False:
            if self.lw.count() == 0:
                return
            self.Preview_Next = True
            rand=random.randint(0, self.lw.count() - 1)
            self.lw.setCurrentRow(rand)
            self.mp3_url = self.SongList[rand][1]
            self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
            self.qsl.setValue(0)
            self.MusicPlay()
            self.Preview_Next = False

    def OpenMusic(self):
        directory = QFileDialog.getExistingDirectory(
                        self,
                        "Выбрать папку с музыкой",
                        os.getcwd(),
                        QFileDialog.ShowDirsOnly
        )
        if directory:
            self.AddListItems(directory)
            self.mp3_url = ''
            self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
            self.lb1.setText('00:00')
            self.lb2.setText('00:00')
            self.qsl.setSliderPosition(0)
            self.Play_Pause = True

    def AddListItems(self, directory):
        self.lw.clear()
        # Запишите музыкальный каталог в файл конфигурации для следующего удобного использования
        config = configparser.ConfigParser()
        config.read("Setting.ini")
        if not os.path.exists('Setting.ini'):
            config.add_section("Music")
        config.set("Music", "PATH", directory)
        config.write(open("Setting.ini", "w"))

        for songname in os.listdir(directory):
            if '.mp3' in songname:
                Song=[songname,(directory+'\\'+songname).replace('\\','/')]
                self.SongList.append(Song)
                self.lw.addItem(Song[0])
        self.lw.setCurrentRow(0)
        if not self.SongList:
            self.mp3_url = self.SongList[self.lw.currentRow()][1]

    # Дважды щелкните, чтобы воспроизвести музыку
    def MouseDoubleClick(self):
        print("  7 MouseDoubleClick")
        self.qsl.setValue(0)
        self.Preview_Next = True
        self.mp3_url = self.SongList[self.lw.currentRow()][1]
        self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
        self.MusicPlay()
        self.Preview_Next = False

    def Message(self):
        QMessageBox.about(self,"Сообщение", "В настоящее время нет музыки.")

    # Воспроизведение и пауза
    def MusicPlay(self):
        if self.lw.count()==0:
            self.Message()
            return

        if self.player.isAudioAvailable()==False:
            self.mp3_url = self.SongList[self.lw.currentRow()][1]
            self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))

        if self.Play_Pause==True or self.Preview_Next==True:
            self.player.play()
            self.Play_Pause=False
            self.btn_play.setText('Пауза')
        elif self.Play_Pause==False and self.Preview_Next==False:
            self.player.pause()
            self.Play_Pause=True
            self.btn_play.setText('Воспроизведение')

    # Предыдущая песня
    def MusicPreview(self):
        self.qsl.setValue(0)
        if self.lw.count()==0:
            self.Message()
            return

        if self.lw.currentRow()!=0:
            self.lw.setCurrentRow(self.lw.currentRow()-1)
            self.Preview_Next = True
            self.mp3_url = self.SongList[self.lw.currentRow()][1]
            self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
            self.MusicPlay()
            self.Preview_Next = False
        else:
            self.lw.setCurrentRow(self.lw.count() - 1)
            self.Preview_Next = True
            self.mp3_url = self.SongList[self.lw.currentRow()][1]
            self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
            self.MusicPlay()
            self.Preview_Next = False

    # Следующая песня
    def MusicNext(self):
        self.qsl.setValue(0)
        if self.lw.count()==0:
            self.Message()
            return

        if self.lw.currentRow() != self.lw.count()-1:
            self.lw.setCurrentRow(self.lw.currentRow()+1)
            self.Preview_Next = True
            self.mp3_url      = self.SongList[self.lw.currentRow()][1]
            self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
            self.MusicPlay()
            self.Preview_Next = False
        else:
            self.lw.setCurrentRow(0)
            self.Preview_Next = True
            self.mp3_url      = self.SongList[self.lw.currentRow()][1]
            self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
            self.MusicPlay()
            self.Preview_Next = False


if __name__=='__main__':
    app  = QApplication(sys.argv)
    app.setStyle("fusion")
    w    = MyMusicApp()
    icon = QIcon()
    icon.addPixmap(QPixmap("myicon.ico"), QIcon.Normal, QIcon.Off)
    w.setWindowIcon(icon)
    w.setWindowTitle('Музыкальный проигрыватель.')
    w.show()
    sys.exit(app.exec_())