[app]
title = Mon App Simple
package.name = monappsimple
package.domain = org.exemple
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

# Ces deux lignes règlent l'erreur des outils 37 en forçant la version 34
android.api = 34
android.build_tools_version = 34.0.0

orientation = portrait
osx.kivy_version = 2.3.0
fullscreen = 1
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
