import sys

from PySide6.QtCore import (
    Qt,
    QSysInfo,
    QSettings,
    QRectF,
)
from PySide6.QtGui import (
    QAction,
    QIcon,
    QShortcut,
    QKeySequence,
    QActionGroup,
    QCloseEvent,
    QPainter,
    QStandardItemModel,
    QStandardItem,
)
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QTabWidget,
    QMessageBox,
    QTextEdit,
    QFileDialog,
    QToolBar,
    QComboBox,
    QGraphicsItem,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsRectItem,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTreeView,
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        
        if QSysInfo.productType() == "windows":
            self.setWindowIcon(QIcon("./_internal/bem_instructionals_CCbysa.ico"))
        elif QSysInfo.productType() == "osx":
            self.setWindowIcon(QIcon("bem_instructionals_CCbysa.icns"))
        elif QSysInfo.productType() == "linux":
            self.setWindowIcon(QIcon("bem_instructionals_CCbysa.png"))
        #else the OS is unknown and the window icon won't be set
        
        l = QLabel("My simple app.")
        l.setMargin(10)
        self.setCentralWidget(l)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())