from PyQt5.QtCore import pyqtProperty, QObject, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtQuick import QQuickWindow, QQuickItem

from OpenGL import GL
from OpenGL.GL.GREMEDY.string_marker import *

class MainWindow(QQuickWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self._app = None
        self._backgroundColor = QColor(204, 204, 204, 255)

        self.setClearBeforeRendering(False)
        self.beforeRendering.connect(self._render, type=Qt.DirectConnection)

    def getApplication(self):
        return self._app

    def setApplication(self, app):
        self._app = app

    application = pyqtProperty(QObject, fget=getApplication, fset=setApplication)

    def getBackgroundColor(self):
        return self._backgroundColor

    def setBackgroundColor(self, color):
        self._backgroundColor = color

    backgroundColor = pyqtProperty(QColor, fget=getBackgroundColor, fset=setBackgroundColor)

    def _render(self):
        if bool(glStringMarkerGREMEDY):
            msg = b"Begin Rendering Background"
            glStringMarkerGREMEDY(len(msg), msg)

        GL.glClearColor(self._backgroundColor.redF(), self._backgroundColor.greenF(), self._backgroundColor.blueF(), self._backgroundColor.alphaF())
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        if self._app:
            self._app.getController().getActiveView().render()

        if bool(glStringMarkerGREMEDY):
            msg = "End Rendering Background"
            glStringMarkerGREMEDY(len(msg), msg)