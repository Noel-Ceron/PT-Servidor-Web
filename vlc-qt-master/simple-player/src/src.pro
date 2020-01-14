#
# VLC-Qt Simple Player
# Copyright (C) 2015 Tadej Novak <tadej@tano.si>
#

TARGET      = simple-player
TEMPLATE    = app
CONFIG 	   += c++11

QT         += core gui widgets

SOURCES    += main.cpp \
    SimplePlayer.cpp

HEADERS    += SimplePlayer.h

FORMS      += SimplePlayer.ui

LIBS       += -lVLCQtCore -lVLCQtWidgets


# Edit below for custom library location
LIBS       += -L/usr/local/lib -lVLCQtCore -lVLCQtWidgets
INCLUDEPATH += /usr/local/include
