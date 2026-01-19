[app]
# (str) Title of your application
title = System Update

# (str) Package name
package.name = sysupdate

# (str) Package domain (needed for android packaging)
package.domain = org.security

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
# Comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
# Yahan hum saari zaruri permissions mang rahe hain
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, ACCESS_FINE_LOCATION

# (int) Android API to use (21 is usually good for broad support)
android.api = 31

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
