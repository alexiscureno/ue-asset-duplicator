import sys
import unreal
import os
import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QCheckBox, QSpinBox
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QSize
from PyQt5.QtGui import QImage, QPixmap, QMouseEvent
from PyQt5 import uic, QtCore

def duplicate(assets):
    start_time = time.time()

    # Instantiate the Unreal Engine classes.
    editor_util = unreal.EditorUtilityLibrary()
    editor_asset_lib = unreal.EditorAssetLibrary()

    # Get the selected assets in the Unreal Editor.
    selected_assets = editor_util.get_selected_assets()

    # Get the number of selected assets.
    num_assets = len(selected_assets)

    # Set the number of times each asset will be duplicated.
    num_copies = assets

    # Calculate the total number of copies that will be made.
    total_num_copies = num_assets * num_copies

    # Set the label to display in the progress dialog.
    text_label = "Duplicating Assets"

    # Set the variable that will be used to determine if the script is still running.
    running = True

    # Use the ScopedSlowTask context manager to create a progress dialog that displays the progress of the script.
    with unreal.ScopedSlowTask(total_num_copies, text_label) as slow_task:
        # Display the progress dialog.
        slow_task.make_dialog(True)

        # Iterate through each selected asset.
        for asset in selected_assets:
            # Get the name and path of the asset to be duplicated.
            asset_name = asset.get_fname()
            asset_path = editor_asset_lib.get_path_name_for_loaded_asset(asset)
            source_path = os.path.dirname(asset_path)

            # Iterate the specified number of times to duplicate the asset.
            for i in range(num_copies):

                # If the user presses the cancel button, stop the script.
                if slow_task.should_cancel():
                    running = False
                    break
                # Generate a new name and path for the duplicated asset.
                new_name = "{}_{}".format(asset_name, i)
                dest_path = os.path.join(source_path, new_name)

                # Duplicate the asset.
                duplicate = editor_asset_lib.duplicate_asset(asset_path, dest_path)

                # Update the progress dialog.
                slow_task.enter_progress_frame(1)

                # If the duplicate already exists, log a message to the console.
                if duplicate is None:
                    unreal.log('Duplicate from {} at {} already exists'.format(source_path, dest_path))
            # If the script has been cancelled, break out of the loop.
            if not running:
                break

        # Get the time again and calculate the elapsed time.
        end_time = time.time()
        # Log a message to the console indicating the number of assets duplicated and the time taken to execute the script.
        unreal.log('{} assets duplicated {} times in {} seconds'.format(num_assets, num_copies, end_time - start_time))


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r"F:\PycharmProjects\UE\ue-asset-duplicator\asset-duplicator.ui", self)

        # Spinbox
        self.spinbox = self.findChild(QSpinBox, "spinBox")
        # Buttons
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.clicked_)

    def clicked_(self):

        num_assets = self.spinbox.value()
        duplicate(num_assets)
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
