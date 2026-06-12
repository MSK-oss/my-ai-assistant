[app]
title = AI Assistant
package.name = aiagent
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy,pyjnius,requests
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET,RECORD_AUDIO,WAKE_LOCK,FOREGROUND_SERVICE
services = AIBrain:service.py
android.api = 33
android.minapi = 24
android.ndk = 25c
android.accept_sdk_license = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
