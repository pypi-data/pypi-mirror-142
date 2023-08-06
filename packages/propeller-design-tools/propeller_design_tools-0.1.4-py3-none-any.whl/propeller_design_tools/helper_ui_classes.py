import os
from propeller_design_tools.user_settings import get_setting, set_propeller_database, set_airfoil_database
from propeller_design_tools.funcs import count_airfoil_db, count_propeller_db
import sys
from io import StringIO
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
try:
    from PyQt5 import QtWidgets, QtCore
except:
    pass


class SingleAxCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(SingleAxCanvas, self).__init__(fig)


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


class PDT_GroupBox(QtWidgets.QGroupBox):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10

        super(PDT_GroupBox, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)


class PDT_Label(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10
        width = kwargs.pop('width') if 'width' in kwargs else None

        super(PDT_Label, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)
        self.set_width(width=width)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_width(self, width: int):
        if width is not None:
            self.setFixedWidth(width)


class PDT_CheckBox(QtWidgets.QCheckBox):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10

        super(PDT_CheckBox, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)


class PDT_PushButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10
        width = kwargs.pop('width') if 'width' in kwargs else None

        super(PDT_PushButton, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)
        self.set_width(width=width)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_width(self, width: int):
        if width is not None:
            self.setFixedWidth(width)


class PDT_LineEdit(QtWidgets.QLineEdit):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10
        width = kwargs.pop('width') if 'width' in kwargs else None

        super(PDT_LineEdit, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)
        self.set_width(width=width)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_width(self, width: int):
        if width is not None:
            self.setFixedWidth(width)


class PDT_ComboBox(QtWidgets.QComboBox):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10
        width = kwargs.pop('width') if 'width' in kwargs else None

        super(PDT_ComboBox, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)
        self.set_width(width=width)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_width(self, width: int):
        if width is not None:
            self.setFixedWidth(width)


class PDT_TextEdit(QtWidgets.QTextEdit):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10
        width = kwargs.pop('width') if 'width' in kwargs else None
        height = kwargs.pop('height') if 'height' in kwargs else None
        read_only = kwargs.pop('read_only') if 'read_only' in kwargs else True

        super(PDT_TextEdit, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)
        self.set_width(width=width)
        self.set_height(height=height)
        self.set_read_only(read_only=read_only)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_width(self, width: int):
        if width is not None:
            self.setFixedWidth(width)

    def set_height(self, height: int):
        if height is not None:
            self.setFixedHeight(height)

    def set_read_only(self, read_only: bool):
        self.setReadOnly(read_only)


class DatabaseSelectionWidget(QtWidgets.QWidget):
    def __init__(self, main_win: 'InterfaceMainWindow', db_type: str, db_dir: str = None):
        super(DatabaseSelectionWidget, self).__init__()
        self.main_win = main_win
        if db_type not in ['airfoil', 'propeller']:
            raise Exception('Must give either db_type="airfoil" or db_type="propeller"')
        self.db_type = db_type
        self.db_dir = db_dir

        lay = QtWidgets.QHBoxLayout()
        self.setLayout(lay)

        self.current_db_lbl = PDT_Label('', font_size=11)
        lay.addWidget(self.current_db_lbl)

        set_btn = PDT_PushButton('...', width=50, font_size=11)
        set_btn.clicked.connect(self.set_btn_clicked)
        lay.addWidget(set_btn)

        self.found_lbl = PDT_Label('', font_size=11)
        lay.addWidget(self.found_lbl)

    @property
    def found_files(self):
        if self.db_type == 'airfoil':
            return count_airfoil_db()
        else:  # self.db_type == 'propeller'
            return count_propeller_db()

    @property
    def found_txt(self):
        return '{} {}(s) found!'.format(self.found_files, self.db_type)

    def get_existing_setting(self):
        return get_setting(s='{}_database'.format(self.db_type))

    def set_current_db(self, db_dir: str = None):
        if db_dir is None:
            db_dir = self.get_existing_setting()

        self.current_db_lbl.setText(db_dir)
        self.db_dir = db_dir

        with Capturing() as output:
            if self.db_type == 'airfoil':
                set_airfoil_database(path=db_dir)
            else:   # db_type == 'propeller'
                set_propeller_database(path=db_dir)

        self.main_win.console_te.append('\n'.join(output))
        self.found_lbl.setText(self.found_txt)

    def set_btn_clicked(self):
        cap = 'Set {} database directory'.format(self.db_type)
        start_dir = os.getcwd()
        direc = QtWidgets.QFileDialog.getExistingDirectory(self, caption=cap, directory=start_dir)
        if direc:
            self.set_current_db(db_dir=direc)


class RangeLineEditWidget(QtWidgets.QWidget):
    def __init__(self):
        super(RangeLineEditWidget, self).__init__()
        lay = QtWidgets.QHBoxLayout()
        self.setLayout(lay)
        self.left_le = PDT_LineEdit('', font_size=12, width=100)
        self.right_le = PDT_LineEdit('', font_size=12, width=100)

        lay.addWidget(self.left_le)
        lay.addWidget(PDT_Label('->', font_size=12))
        lay.addWidget(self.right_le)
        lay.addStretch()


class AxesComboBoxWidget(QtWidgets.QWidget):
    def __init__(self):
        super(AxesComboBoxWidget, self).__init__()
        lay = QtWidgets.QHBoxLayout()
        self.setLayout(lay)

        self.yax_cb = PDT_ComboBox(width=100)
        af_plopts = ['alpha', 'CL', 'CD', 'CDp', 'CM', 'Top_Xtr', 'Bot_Xtr', 'CL/CD']
        self.yax_cb.addItems(['y-axis'] + af_plopts)
        lay.addWidget(self.yax_cb)
        lay.addWidget(PDT_Label('versus'))
        self.xax_cb = PDT_ComboBox(width=100)
        self.xax_cb.addItems(['x-axis'] + af_plopts)
        lay.addWidget(self.xax_cb)
        lay.addStretch()


class FoilDataPointWidget(QtWidgets.QWidget):
    def __init__(self, main_win: 'InterfaceMainWindow'):
        super(FoilDataPointWidget, self).__init__()
        self.main_win = main_win

        lay = QtWidgets.QFormLayout()
        self.setLayout(lay)

        overwrite_chk = PDT_CheckBox('Overwrite Existing Data?', font_size=11)
        lay.addRow(PDT_Label('Add Datapoint Range:', font_size=14), overwrite_chk)
        lay.addRow(PDT_Label('Ncrit:', font_size=12), RangeLineEditWidget())
        lay.addRow(PDT_Label('Re:', font_size=12), RangeLineEditWidget())
        lay.addRow(PDT_Label('Mach:', font_size=12), RangeLineEditWidget())

        add_btn = PDT_PushButton('Add Data', font_size=12, width=110)
        clear_btn = PDT_PushButton('Clear Ranges', font_size=12, width=130)
        btn_lay = QtWidgets.QHBoxLayout()
        btn_lay.addStretch()
        btn_lay.addWidget(add_btn)
        btn_lay.addWidget(clear_btn)
        btn_lay.addStretch()
        lay.addRow(btn_lay)
        lay.setAlignment(btn_lay, QtCore.Qt.AlignRight)
        lay.setLabelAlignment(QtCore.Qt.AlignRight)
