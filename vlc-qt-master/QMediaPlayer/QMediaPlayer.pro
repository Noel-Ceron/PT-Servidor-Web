#-------------------------------------------------
#
# Project created by QtCreator 2018-11-01T18:58:15
#
#-------------------------------------------------


QT       += core gui multimedia multimediawidgets

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = QMediaPlayer
TEMPLATE = app

CONFIG += c++11

SOURCES += main.cpp \
        widget.cpp

HEADERS += widget.h \

FORMS += widget.ui

QMAKE_CXXFLAGS += -std=gnu++11


LIBS       += -lVLCQtCore -lVLCQtWidgets

LIBS       += -L/usr/local/lib -lVLCQtCore -lVLCQtWidgets
INCLUDEPATH += /usr/local/include
