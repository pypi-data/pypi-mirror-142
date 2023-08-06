from propeller_design_tools.funcs import get_all_airfoil_files, get_all_propeller_dirs
try:
    from PyQt5 import QtWidgets
    from propeller_design_tools.helper_ui_classes import PDT_TextEdit, Capturing, \
        PDT_GroupBox, PDT_Label, PDT_PushButton, PDT_ComboBox, DatabaseSelectionWidget, \
        SingleAxCanvas
except:
    pass


class InterfaceMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(InterfaceMainWindow, self).__init__()
        self.setWindowTitle('PDT Control Dashboard')
        self.setMinimumSize(1400, 800)

        # central widget
        center_widg = QtWidgets.QWidget()
        center_lay = QtWidgets.QVBoxLayout()
        center_widg.setLayout(center_lay)
        self.setCentralWidget(center_widg)

        # the main groups
        sett_grp = PDT_GroupBox('Settings'.upper(), italic=True, font_size=16)
        center_lay.addWidget(sett_grp)
        af_grp = PDT_GroupBox('Airfoil Analysis'.upper(), italic=True, font_size=16)
        center_lay.addWidget(af_grp)
        prop_grp = PDT_GroupBox('Propellers'.upper(), italic=True, font_size=16)
        center_lay.addWidget(prop_grp)
        console_grp = PDT_GroupBox('Console Output'.upper(), italic=True, font_size=16)
        center_lay.addWidget(console_grp)

        # settings group
        sett_lay = QtWidgets.QFormLayout()
        sett_grp.setLayout(sett_lay)
        af_db_select_widg = DatabaseSelectionWidget(main_win=self, db_type='airfoil')
        sett_lay.addRow(PDT_Label('Airfoil Database:', font_size=14), af_db_select_widg)
        prop_db_select_widg = DatabaseSelectionWidget(main_win=self, db_type='propeller')
        sett_lay.addRow(PDT_Label('Propeller Database:', font_size=14), prop_db_select_widg)

        # airfoil group
        af_lay = QtWidgets.QHBoxLayout()
        af_grp.setLayout(af_lay)
        af_left_lay = QtWidgets.QVBoxLayout()
        af_lay.addLayout(af_left_lay)
        af_center_lay = QtWidgets.QVBoxLayout()
        af_lay.addLayout(af_center_lay)
        af_right_lay = QtWidgets.QVBoxLayout()
        af_lay.addLayout(af_right_lay)

        # airfoil left
        af_left_top_lay = QtWidgets.QFormLayout()
        af_left_lay.addLayout(af_left_top_lay)
        af_left_lay.addStretch(1)
        select_foil_cb = PDT_ComboBox(width=200)
        select_foil_cb.addItems(get_all_airfoil_files())
        af_left_top_lay.addRow(PDT_Label('Select Foil:', font_size=14), select_foil_cb)

        # airfoil center
        self.foil_xy_canvas = SingleAxCanvas(self, width=4.5, height=4)
        af_center_lay.addWidget(self.foil_xy_canvas)

        #airfoil right
        self.foil_metric_canvas = SingleAxCanvas(self, width=4.5, height=4)
        af_right_lay.addWidget(self.foil_metric_canvas)

        # propeller group
        prop_lay = QtWidgets.QHBoxLayout()
        prop_grp.setLayout(prop_lay)

        # console group
        console_lay = QtWidgets.QVBoxLayout()
        console_grp.setLayout(console_lay)
        self.console_te = PDT_TextEdit()
        console_lay.addWidget(self.console_te)
        clear_console_btn = PDT_PushButton('Clear', font_size=11, width=100)
        clear_console_btn.clicked.connect(self.clear_console_btn_clicked)
        console_lay.addWidget(clear_console_btn)

        # call these last because they rely on self.console_te existing
        af_db_select_widg.set_current_db()
        prop_db_select_widg.set_current_db()

    def clear_console_btn_clicked(self):
        self.console_te.clear()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = InterfaceMainWindow()
    w.show()
    app.exec_()
