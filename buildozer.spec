[app]

# (str) Title of your application
title = My Gym App

# (str) Package name
package.name = mygymapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.myself

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Entry point of the application
entrypoint = main.py

# (str) Presplash of the application
presplash.filename = presplash.png

# (str) Icon of the application
icon.filename = icon.png

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Android permissions
android.permissions = INTERNET

# (str) Bootstrap used for android builds
# android: python3, sdl2
# default: sdl2
p4a.bootstrap = sdl2
