from propeller_design_tools.funcs import get_all_airfoil_files, get_all_propeller_dirs
from propeller_design_tools.airfoil import Airfoil
try:
    from PyQt5 import QtWidgets
    from propeller_design_tools.helper_ui_classes import PDT_TextEdit, Capturing, \
        PDT_GroupBox, PDT_Label, PDT_PushButton, PDT_ComboBox, DatabaseSelectionWidget, \
        SingleAxCanvas, FoilDataPointWidget, AxesComboBoxWidget, ExistingFoilDataWidget
except:
    pass


class InterfaceMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(InterfaceMainWindow, self).__init__()
        self.setWindowTitle('PDT Control Dashboard')
        self.setMinimumSize(1400, 800)
        self.foil = None

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
        af_left_lay.addStretch()
        self.exist_data_widg = ExistingFoilDataWidget(main_win=self)
        af_left_lay.addWidget(self.exist_data_widg)
        af_left_lay.addStretch()
        add_foil_data_widg = FoilDataPointWidget(main_win=self)
        add_foil_data_widg.add_btn.clicked.connect(self.add_foil_data_btn_clicked)
        add_foil_data_widg.clear_btn.clicked.connect(self.clear_foil_ranges_btn_clicked)
        af_left_lay.addWidget(add_foil_data_widg)
        af_left_lay.addStretch()

        # airfoil center
        af_center_top_lay = QtWidgets.QFormLayout()
        af_center_lay.addLayout(af_center_top_lay)
        select_foil_cb = PDT_ComboBox(width=150)
        select_foil_cb.addItems(['None'] + get_all_airfoil_files())
        select_foil_cb.currentTextChanged.connect(self.select_foil_cb_changed)
        af_center_top_lay.addRow(PDT_Label('Select Foil:', font_size=14), select_foil_cb)
        self.foil_xy_canvas = SingleAxCanvas(self, width=4, height=4)
        af_center_lay.addWidget(self.foil_xy_canvas)

        #airfoil right
        af_right_top_lay = QtWidgets.QFormLayout()
        af_right_lay.addLayout(af_right_top_lay)
        ax_cb_widg = AxesComboBoxWidget()
        self.af_yax_cb, self.af_xax_cb = ax_cb_widg.yax_cb, ax_cb_widg.xax_cb
        self.af_yax_cb.currentTextChanged.connect(self.af_metric_cb_changed)
        self.af_xax_cb.currentTextChanged.connect(self.af_metric_cb_changed)
        af_right_top_lay.addRow(PDT_Label('Plot Metric:', font_size=14), ax_cb_widg)

        self.foil_metric_canvas = SingleAxCanvas(self, width=8, height=4.5)
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

    def af_metric_cb_changed(self):
        self.foil_metric_canvas.axes.clear()
        y_txt, x_txt = self.af_yax_cb.currentText(), self.af_xax_cb.currentText()
        if y_txt == 'y-axis' or x_txt == 'x-axis':
            return

        if self.foil is not None:
            with Capturing() as output:
                self.foil.plot_polar_data(x_param=x_txt, y_param=y_txt, fig=self.foil_metric_canvas.figure)
            self.console_te.append('\n'.join(output))
            self.foil_metric_canvas.draw()

    def clear_console_btn_clicked(self):
        self.console_te.clear()

    def select_foil_cb_changed(self, foil_txt):
        self.foil_xy_canvas.axes.clear()
        with Capturing() as output:
            self.foil = Airfoil(name=foil_txt, exact_namematch=True)
            self.foil.plot_geometry(fig=self.foil_xy_canvas.figure)
        self.console_te.append('\n'.join(output))
        self.foil_xy_canvas.draw()

        self.af_metric_cb_changed()  # updates the metric plot
        self.exist_data_widg.update_airfoil(af=self.foil)

    def add_foil_data_btn_clicked(self):
        print('here')

    def clear_foil_ranges_btn_clicked(self):
        print('here2')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = InterfaceMainWindow()
    w.show()
    app.exec_()
