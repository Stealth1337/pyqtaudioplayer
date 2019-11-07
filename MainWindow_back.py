# Пофиксил тайм-лайн. Теперь можно перемещать слайдер.
# Пофиксил текущее время и полное время трека.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtCore import *
from MainWindow import Ui_MainWindow
from msgBox import MsgBox_MainWindow
import os.path
import time as t


class MyWidget(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.player = QMediaPlayer()
        self.play_or_pause = True
        self.nextTrack = False
        self.url_track = ''
        self.is_muted = False
        self.is_repeat = False
        self.is_default, self.is_black, self.is_orange = True, False, False

        # listTracks и tracklist различаются.
        # Создаём список треков, состоящий из списков (название, ссылка)

        self.tracklist = []

        self.timer = QTimer()
        self.timer.timeout.connect(self.PlayBackMode)
        self.timer.start(1000)
        self.AddTracksFromFile()
        self.action_3.triggered.connect(self.open_file)
        self.action_4.triggered.connect(self.DirectoryTracks)
        self.StyleBlack.triggered.connect(self.style_black)
        self.StyleDefault.triggered.connect(self.style_default)
        self.StyleOrange.triggered.connect(self.style_orange)
        self.StyleBlack.triggered.connect(self.black)
        self.StyleDefault.triggered.connect(self.default)
        self.StyleOrange.triggered.connect(self.orange)
        self.horizontalSlider.sliderMoved[int].connect(
            self.CurrentPositionTrack)
        self.volSlider.sliderMoved[int].connect(self.CurrentVolumeTrack)
        self.volSlider.valueChanged[int].connect(self.CurrentVolumeTrack)
        self.buttonPlay.clicked.connect(self.PlayPauseMode)
        self.buttonNext.clicked.connect(self.NextTrack)
        self.buttonBack.clicked.connect(self.PreviousTrack)
        self.buttonPause.clicked.connect(self.func_repeat)
        self.player.setVolume(40)
        self.volSlider.setValue(40)
        self.msg = MsgBox()
        self.iconLabel = QPixmap(
            'C:/Users/Sh3ll/Desktop/miniwinAmp/icons/volume.png')
        self.iconVolume.setPixmap(self.iconLabel)
        self.setMouseTracking(True)

    def PlayBackMode(self):
        if not self.play_or_pause:
            # Задаём начальное положение слайдера с длительностью
            self.horizontalSlider.setMinimum(0)
            # Так же задаём максимальное положение слайдера
            self.horizontalSlider.setMaximum(self.player.duration())
            self.horizontalSlider.setValue(
                self.horizontalSlider.value() + 1000)
        print(self.listTracks.currentRow())
        # Задаём минуты и секунды лейблам для длительности трека.
        self.fullTimeLabel.setText(
            t.strftime('%M:%S', t.localtime(self.player.duration() / 1000)))
        self.currentTimeLabel.setText(
            t.strftime('%M:%S', t.localtime(self.player.position() / 1000)))
        if self.player.duration() != 0 and\
                self.player.position() == self.player.duration()\
                and self.is_repeat:
            self.play_or_pause = True
            self.horizontalSlider.setValue(0)
            self.listTracks.setCurrentRow(self.listTracks.currentRow())
            self.url_track = self.tracklist[self.listTracks.currentRow()][1]
            self.player.setMedia(QMediaContent(QUrl(self.url_track)))
            self.PlayPauseMode()
        if self.player.duration() != 0 and\
                self.player.position() == self.player.duration()\
                and self.listTracks.currentRow() != self.listTracks.count() - 1:
            self.play_or_pause = True
            self.horizontalSlider.setValue(0)
            self.listTracks.setCurrentRow(self.listTracks.currentRow() + 1)
            self.url_track = self.tracklist[self.listTracks.currentRow()][1]
            self.player.setMedia(QMediaContent(QUrl(self.url_track)))
            self.PlayPauseMode()
        if self.player.duration() != 0 and\
                self.player.position() == self.player.duration()\
                and self.listTracks.currentRow() == self.listTracks.count() - 1:
            self.play_or_pause = True
            self.horizontalSlider.setValue(0)
            self.listTracks.setCurrentRow(0)
            print(self.listTracks.currentRow())
            self.url_track = self.tracklist[self.listTracks.currentRow()][1]
            self.player.setMedia(QMediaContent(QUrl(self.url_track)))
            self.PlayPauseMode()


    # Запуск/Пауза трека.
    def PlayPauseMode(self):
        if self.listTracks.count() == 0:
            self.msg.show()
            return

        elif not self.player.isAudioAvailable():
            self.url_track = self.tracklist[self.listTracks.currentRow()][1]
            self.player.setMedia(QMediaContent(QUrl(self.url_track)))
        if self.play_or_pause:
            self.player.play()
            self.play_or_pause = False
            self.buttonPlay.setIcon(self.icon3)
        elif not self.play_or_pause:
            self.player.pause()
            self.play_or_pause = True
            self.buttonPlay.setIcon(self.icon2)

    # Работа со слайдерами (смена значения)

    def CurrentPositionTrack(self):
        self.player.setPosition(self.horizontalSlider.value())

    def CurrentVolumeTrack(self):
        self.player.setVolume(self.volSlider.value())

        if self.volSlider.value() == 0:
            if self.is_default or self.is_orange:
                self.iconLabel = QPixmap(
                    'C:/Users/Sh3ll/Desktop/miniwinAmp/icons/volume_mute.png')
                self.iconVolume.setPixmap(self.iconLabel)
            else:
                self.iconLabel = QPixmap(
                    'C:/Users/Sh3ll/Desktop/miniwinAmp/icons/volume_mute_white.png')
                self.iconVolume.setPixmap(self.iconLabel)
        else:
            if self.is_default or self.is_orange:
                self.iconLabel = QPixmap(
                    'C:/Users/Sh3ll/Desktop/miniwinAmp/icons/volume.png')
                self.iconVolume.setPixmap(self.iconLabel)
            else:
                self.iconLabel = QPixmap(
                    'C:/Users/Sh3ll/Desktop/miniwinAmp/icons/volume_white.png')
                self.iconVolume.setPixmap(self.iconLabel)

    # Проигрывание трека двойным кликом мыши.
    def DoubleClickPlay(self):
        self.url_track = self.tracklist[self.listTracks.currentRow()][1]
        self.listTracks.setCurrentRow(self.listTracks.currentRow())
        self.player.setMedia(QMediaContent(QUrl(self.url_track)))
        self.nextTrack = True
        self.horizontalSlider.setValue(0)
        self.play_or_pause = True
        self.PlayPauseMode()

    # Функция диалога для выбора файла.
    def open_file(self):
        file = QFileDialog.getOpenFileName(self, "Open file", "",
                                           "mp3 Audio (*.mp3)")
        if file:
            self.AddNameTrack(file)
            self.url_track = ''
            self.player.setMedia(QMediaContent(QUrl(self.url_track)))

    # Добавление треков.

    def AddTracksFromFile(self):
        with open('songbase.txt', 'r') as file:
            if not file:
                print('Пустая база треков')
            else:
                for line in file:
                    line = line.replace('\n', '').split(';')
                    if os.path.exists(line[1]):
                        self.listTracks.addItem(line[0])
                        self.tracklist.append(line)
                        print(self.tracklist)
            self.listTracks.setCurrentRow(0)

    # Добавление трека в listTracks (Плейлист)
    def AddNameTrack(self, file):
        if '.mp3' in file[0]:
            songname = file[0]
            track = [songname[songname.rfind('/') + 1:songname.find('.mp3')],
                     songname.replace('\\', '/')]
            print(track)
            with open('songbase.txt', 'r') as file1:
                for line in file1:
                    if songname in line:
                        return
            with open('songbase.txt', 'a') as file1:
                file1.write(f'{track[0]};{track[1]}\n')
            self.tracklist.append(track)
            self.listTracks.addItem(track[0])
        self.listTracks.setCurrentRow(0)

    def DirectoryTracks(self):
        directory = QFileDialog.getExistingDirectory(
            self,
            "Выбрать папку с музыкой",
            os.getcwd(),
            QFileDialog.ShowDirsOnly
        )
        if directory:
            self.addDirectory(directory)
            self.url_track = ''
            self.player.setMedia(QMediaContent(QUrl(self.url_track)))
            self.currentTimeLabel.setText('00:00')
            self.fullTimeLabel.setText('00:00')
            self.horizontalSlider.setSliderPosition(0)
            self.play_or_pause = True

    def addDirectory(self, directory):
        for songname in os.listdir(directory):
            if '.mp3' in songname:
                track = [
                    songname[songname.rfind('/') + 1:songname.find('.mp3')],
                    (directory+'\\'+songname).replace('\\','/')]
                with open('songbase.txt', 'r') as file1:
                    for line in file1:
                        if songname in line:
                            return
                with open('songbase.txt', 'a') as file1:
                    file1.write(f'{track[0]};{track[1]}\n')
                self.tracklist.append(track)
                self.listTracks.addItem(track[0])
        self.listTracks.setCurrentRow(0)
        if not self.tracklist:
            self.url_track = self.SongList[self.lw.currentRow()][1]

    # Следующий трек
    def NextTrack(self):
        self.horizontalSlider.setValue(0)
        if self.listTracks.count() == 0:
            self.msg.show()
            return

        elif (self.listTracks.count() - 1) \
                != self.listTracks.currentRow():
            self.listTracks.setCurrentRow(self.listTracks.currentRow() + 1)
            self.url_track = self.tracklist[self.listTracks.currentRow()][1]
            self.player.setMedia(QMediaContent(QUrl(self.url_track)))
            self.play_or_pause = True
            self.PlayPauseMode()
        # Если пришли в конец плейлиста, то возвращаемся в начало плейлиста
        else:
            self.listTracks.setCurrentRow(0)
            self.url_track = self.tracklist[self.listTracks.currentRow()][1]
            self.player.setMedia(QMediaContent(QUrl(self.url_track)))
            self.play_or_pause = True
            self.PlayPauseMode()

    #############################################################

    def func_repeat(self):
        if self.is_repeat:
            self.is_repeat = False
            icon = QIcon()
            icon.addPixmap(QPixmap(
                'C:/Users/Sh3ll/Desktop/miniwinAmp/icons/replay.png'))
            self.buttonPause.setIcon(
                icon)
        else:
            icon = QIcon()
            icon.addPixmap(
                QPixmap(
                    'C:/Users/Sh3ll/Desktop/miniwinAmp/icons/replay_red.png'))
            self.buttonPause.setIcon(
                icon)
            self.is_repeat = True

    def black(self):
        self.is_default, self.is_black, self.is_orange = False, True, False
        self.CurrentVolumeTrack()

    def orange(self):
        self.is_default, self.is_black, self.is_orange = False, False, True
        self.CurrentVolumeTrack()

    def default(self):
        self.is_default, self.is_black, self.is_orange = True, False, False
        self.CurrentVolumeTrack()

    #############################################################

    # Предыдущий трек
    def PreviousTrack(self):
        self.horizontalSlider.setValue(0)
        if self.listTracks.count() == 0:
            self.msg.show()
            return

        elif self.listTracks.currentRow() == 0:
            self.listTracks.setCurrentRow(self.listTracks.count() - 1)
            self.url_track = self.tracklist[self.listTracks.currentRow()][1]
            self.player.setMedia(QMediaContent(QUrl(self.url_track)))
            self.play_or_pause = True
            self.PlayPauseMode()
        else:
            self.listTracks.setCurrentRow(self.listTracks.currentRow() - 1)
            self.url_track = self.tracklist[self.listTracks.currentRow()][1]
            self.player.setMedia(QMediaContent(QUrl(self.url_track)))
            self.play_or_pause = True
            self.PlayPauseMode()


class MsgBox(QMainWindow, MsgBox_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_close.clicked.connect(self.button_close_window)

    def button_close_window(self):
        self.hide()


def my_excepthook(type, value, tback):
    QtWidgets.QMessageBox.critical(
        window, "CRITICAL ERROR", str(value),
        QtWidgets.QMessageBox.Cancel
    )

    sys.__excepthook__(type, value, tback)


sys.excepthook = my_excepthook

app = QApplication(sys.argv)
app.setStyle('Fusion')
palette = QPalette()
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
