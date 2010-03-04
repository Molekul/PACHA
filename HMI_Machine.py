# encoding : utf-8
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 or later of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
#

from PyQt4 import QtCore, QtGui
import HMI_dictate as hd
import PACHA_pixmap as pp
import machine as m
import HMI_supervision as Hsu
import HMI_action as Hac
import HMI_service as Hse

# Signal relay + widget
class MyButton(object):
    ''' This class makes the button ready for link
    between a button click and a parameter '''
    def __init__(self, text = "", value = 0):
        ''' Constructor, wwith args :
        text : label
        value : id sent in the signal
        '''
        self.value = value
        self.Form = QtGui.QWidget()
        self.Form.setObjectName("Form")
        self.Form.resize(180, 32)
        self.button = QtGui.QPushButton(text, self.Form)
        self.button.setGeometry(QtCore.QRect(40, 0, 148, 28))

        self.pix = pp.p_pixmap(self.Form)

        QtCore.QMetaObject.connectSlotsByName(self.Form)

        QtCore.QObject.connect(
            self.button,
            QtCore.SIGNAL('clicked()'),
            self.send)

    def send(self):
        ''' signal, made so as to send another signal (valued) '''
        self.button.emit(QtCore.SIGNAL("ToggleMachineView(int)"), self.value)
        # test code for colors

    def change_level(self, level, scale = []):
        ''' Relays the signal, and is to scale if necessary 
        Substracts one for the first element is 0, not 1'''
        def test_level(lev):
            ''' Helper for filter'''
            return (lev < level)

        if len(scale) != 4:
            if (level < 0 or 2 < level):
                level = 3
        else:
            level = len(filter(test_level, scale))
            if (2 < level):
                level = 3
        self.pix.changeColor(level-1)


class HMI_Machine(object):
    ''' Class to embark Widgets related to a single machine, making the
    final outlook and code easy.
    The HMI element shows machine # number, has a grid widget,
    and a synthex, to be displayed on the general widget
    '''
    def __init__(self, number = 1, name = ""):
        ''' Constructor :
        number of the machine (Id sent via signal)
        name of the interface'''
        self.number  = number
        self.grid    = QtGui.QGridLayout()
        self.widgets = {}
        if (name == ""):
            self.synthex = MyButton("  Machine %d" % (number), number)
        else:
            self.synthex = MyButton(name, number)

    def config(self, machine):
        ''' old config, to disappear soon'''
        dkey = "machine %s : %s"

        host = "192.168.122.14"
        user = "root"
        password = "toto"
        command = "reboot"
        akey = dkey % (host, command)
        label = "Action : %s" % command
        self.widgets[akey] = HMI_action(host, user, password,
                                        command = "reboot",
                                        do_label = label,
                                        feedback_command = "ping %s")
        self.grid.addWidget(self.widgets[akey].wForm, 1, 1, 1, 6)
        max_w = self.widgets[akey].width
        i = 2
        # services
        for a_service in ["ntp", "Apache", "ssh"]:
            bkey = "service %s" % a_service
            self.widgets[bkey] = HMI_service(host, a_service)

            self.grid.addWidget(self.widgets[bkey].wForm, i, 1, 1, 6)
            if (max_w < self.widgets[bkey].width):
                max_w = self.widgets[bkey].width
            i += 1
            # self.RefreshWidget = QtGui.QPushButton("Refresh")
            # self.grid.addWidget(self.RefreshWidget, 25, 1, 1, 4)
            # True config to be made of HMI_line's
        self.dictate = hd.HMI_dictate(host, user, password)
        pos_x = 3 * max_w + 1
        self.grid.addWidget(self.dictate.Form, 1, pos_x, 20, 9)
        self.widget = QtGui.QWidget()
        self.widget.setGeometry(0, 28, 910, 456)
        self.widget.setLayout(self.grid)

    def configure(self, a_machine):
        ''' Configure from a machine object '''
        # Actions
        i = 1
        max_w = 0
        for an_action in a_machine.actions:
            akey = "mach%s_cde%s" % (a_machine.hostname, 
                                     an_action["command"])
            label = "Action : " + an_action["command"]
            self.widgets[akey] = Hac.HMI_action(a_machine.agent,
                                                an_action["command"],
                                                label,
                                                feedback_command = "ping %s")
            self.grid.addWidget(self.widgets[akey].wForm, i, 1, 1, 6)
            if (max_w < self.widgets[akey].width):
                max_w = self.widgets[akey].width

        # supervision
        for a_supervision in a_machine.supervisions:
            akey = "mach%s_svc%s" % (a_machine.hostname,
                                     a_supervision["name"])
            self.widgets[akey] = Hsu.HMI_supervision(a_supervision,
                                                     a_machine.hostname)
        # Services
        for a_service in a_machine.services:
            akey = "mach%s_srv%s" % (a_machine.hostname,
                                     a_service["name"])
            self.widgets[akey] = Hse.HMI_service(
                )
            self.grid.addWidget(self.widgets[bkey].wForm, i, 1, 1, 6)
            if (max_w < self.widgets[akey].width):
                max_w = self.widgets[akey].width
        # Machine has an ssh agent ready for use
        self.dictate = hd.HMI_dictate(a_machine.agent)
        pos_x = 3 * max_w + 1
        self.grid.addWidget(self.dictate.Form, 1, pos_x, 20, 9)
        self.widget = QtGui.QWidget()
        self.widget.setGeometry(0, 28, 910, 456)
        self.widget.setLayout(self.grid)


    def move(self, pos_x, pos_y):
        ''' provides initial position'''
        self.widget.move(pos_x, pos_y + 28)

    def pos(self):
        ''' basically returns... the position of the window '''
        return self.widget.pos()

    def show(self, pos):
        ''' Pos-memorizing show'''
        self.widget.move(pos)
        self.widget.show()

    def hide(self):
        ''' Pos-memorizing hide'''
        pos = self.widget.pos()
        self.widget.hide()
        return pos
