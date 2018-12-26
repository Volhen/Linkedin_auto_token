import sys

import socket

from threading import Thread

from PyQt5 import QtWidgets, QtGui, QtCore, QtNetwork

from form.body_robot import Ui_MainWindow

import parsing_redirect

import aut_url

import settings


class AppWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        
        super(AppWindow, self).__init__()
        
        self.setupUi(self)

        self.push_button()

        self.socket_run()


    # Настройка сокета

    def socket_run(self):

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        
        self._sock.bind((settings.HOST, settings.PORT))

        self._sock.listen(settings.CLIENTS_NUM)


    # Обработчик нажатий кнопок 

    def push_button(self):
        
        self.btn_connect.clicked.connect(self.connect_linkedid)

        self.btn_get_token.clicked.connect(self.clear_web)


    # Настройка прокси сервер

    def connect_proxy(self):

        self.proxy = QtNetwork.QNetworkProxy()

        self.proxy.setType(QtNetwork.QNetworkProxy.HttpProxy)

        self.proxy.setHostName(settings.HOST_PROXY)

        self.proxy.setPort(settings.PORT_PROXY)
        
        QtNetwork.QNetworkProxy.setApplicationProxy(self.proxy)


    # Загрузка авторизации на сайте linkedid + прокси для России

    def connect_linkedid(self):

        self.connect_proxy()

        self.web_display.setUrl(QtCore.QUrl(aut_url.authorization_url()))


    # Прокидуем порт на прослушку Localhost, с целью получения CODE + парсинг = TOKEN   


    def read(self):

        try:

            while True:

                print('server wait for clients')

                client, address = self._sock.accept()

                while True:

                    data = client.recv(settings.BUFFER_SIZE)

                    if data:
                        
                        print('CODE is available')

                        str_code = data.decode(settings.ENCODING)

                        CODE = parsing_redirect.params_to_d(str_code).get('code')

                        TOKEN = aut_url.authorization_code(CODE)

                        text = 'Доступ к токену разрешен, Ваш ТОКЕН:'

                        self.display.insertHtml('<b>{}<b/>'.format(text))

                        self.display.append(TOKEN)

                        print('TOKEN is available')
                       
                        # client.close()

                    elif not data:

                        break

                    if data == "Close" or data == "close":

                        client.close()

                client.close()

        except (OSError, ConnectionResetError, KeyboardInterrupt):

            pass

    
    # запуск основного метода (выделение потока для получения CODE + метод отображения графики QT) 

    def run(self):

        u_thread = Thread(target=self.read, daemon=True)

        u_thread.start()

        self.show() 

       
    def clear_web(self):

        self.web_display.close()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    form = AppWindow()

    form.run()

    sys.exit(app.exec_())
