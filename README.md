# Annotation Union

A plugin to combine annotations in the Dragonfly Open3D World software. Made for the Max Planck Florida Institute for Neuroscience (MPFI) Electron Microscopy core.

## Automatic Installation (Windows)

1. Ensure Python 3.5 or later is installed from [python.org](https://www.python.org). (Disclaimer: the installer was tested with Python 3.11 and 3.12. Other versions should work, but are not guaranteed to work. Python 2 may work).
2. On this webpage, click Code -> Download ZIP
3. Go to your downloads folder and extract the zip file
4. Within the extracted file, run `_install.py` (you may need to right-click -> open with -> Python)
5. Follow the instructions in the installer to install the plugin.

## Manual Installation (All Operating Systems)

1. Open Dragonfly
2. Select Developer -> Python Plugin Generator
3. Select if you want this plugin to be installed for your local user or all users
4. Select "Create New From Existing Plugin"
5. Copy the filepath in the file explorer window it opened
6. Open another file explorer window
7. Go to the filepath and create a new, empty folder called `AnnotationUnion_924df9cb243f11efad78f83441a96bd5`
8. On this webpage, click Code -> Download ZIP
9. Go to your downloads folder and extract the zip file
10. Copy the contents of the zip file to the folder you created (`AnnotationUnion_924...`)
11. Restart Dragonfly

## Usage

To use the plugin:
1. Open Dragonfly and your session
2. On the top bar, click Annotation Union -> Start Annotation Union
3. Select an annotation to append other annotations to (this annotation will be modified). Do not enter anything under the "Name" field
4. Select "Start Annotation Union".
5. Select annotations to append. Click "OK" to append the annotation.
6. When done, click "Cancel". The annotations will be appended to the initial annotation.
