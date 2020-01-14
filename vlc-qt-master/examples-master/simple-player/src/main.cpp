/*
* VLC-Qt Simple Player
* Copyright (C) 2015 Tadej Novak <tadej@tano.si>
*/

#include <QCoreApplication>
#include <QApplication>

#include <VLCQtCore/Common.h>

#include "SimplePlayer.h"

int main(int argc, char *argv[])
{
    QCoreApplication::setApplicationName("VLC-Qt Simple Player");
    QCoreApplication::setAttribute(Qt::AA_X11InitThreads);

    QApplication app(argc, argv);
    VlcCommon::setPluginPath(app.applicationDirPath() + "/plugins");

    SimplePlayer mainWindow;
    mainWindow.show();

    return app.exec();
}
