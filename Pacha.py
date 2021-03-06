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

import gettext, ConfigParser, os
import Pacha_config, Group, Machine
import View_MainWindow

""" Main class (and start point) for application Pacha
"""
class Pacha(object):


    """ Instantiate business objects as described in machines config files
            machineDir  : directory on which to look for config files
            return      : a list of groups (with their machines etc) instanciated regarding the config files
    """
    def init_biz(self, machineDir):

        groups = {}

        for filepath in os.listdir(machineDir):
            if (not filepath.startswith(".")):
                configParser = ConfigParser.ConfigParser()
                configParser.read(machineDir + "/" + filepath)

                groupName = configParser.get("general", "group")
                # If we have never seen this group before then create it
                if (not groupName in groups):
                    groups[groupName] = Group.Group(self.conf, groupName)

                machine = Machine.Machine(self.conf, configParser, groups[groupName])

                groups[groupName].machines.append(machine)

        return groups.values()


    """ Instanciate and initialize the GUI objects
            groups      : list af groups
    """
    def initGUI(self, groups):
        # The application
        app = QtGui.QApplication(sys.argv)

        # Replace pix paths by PixMaps in the conf object
        for i in range(0, 4):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.conf.val["general"]["icon_levels"][i]),
                           QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.conf.val["general"]["icon_levels"][i] = icon

        # Main window
        view_mainWindow = View_MainWindow.View_MainWindow(self, self.conf, groups)

        # MainWindow setup is done. Show it!
        view_mainWindow.show()

        return (app, view_mainWindow)


	""" Asks all machine to kill their threads before exiting
	"""
    def quit_main(self):
        for group in self.groups:
            for machine in group.machines:
                machine.exit()


	""" Application init method
	"""
    def __init__(self, sys):
#        _ = gettext.gettext

        # Load general tech configuration
        configParser = ConfigParser.ConfigParser()
        configParser.read("config/pacha.cfg")
        self.conf = Pacha_config.Pacha_config(configParser)

        # Instantiate Machines based on conf
        self.groups = self.init_biz("config/machines")

        # Initialize GUI
        self.app, self.view = self.initGUI(self.groups)

        # Starts machine threads
    	for group in self.groups:
        	for machine in group.machines:
        		machine.start()


""" Main entry point of Pacha
"""
if __name__ == "__main__":
    import sys
    pacha = Pacha(sys)
    sys.exit(pacha.app.exec_())

# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
