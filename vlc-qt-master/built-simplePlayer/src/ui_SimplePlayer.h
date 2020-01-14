/********************************************************************************
** Form generated from reading UI file 'SimplePlayer.ui'
**
** Created by: Qt User Interface Compiler version 5.9.9
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SIMPLEPLAYER_H
#define UI_SIMPLEPLAYER_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QWidget>
#include <VLCQtWidgets/WidgetVideo.h>

QT_BEGIN_NAMESPACE

class Ui_SimplePlayer
{
public:
    QAction *actionOpenUrl;
    QAction *actionStop;
    QAction *actionPause;
    QWidget *centralwidget;
    QGridLayout *gridLayout_2;
    VlcWidgetVideo *video;

    void setupUi(QMainWindow *SimplePlayer)
    {
        if (SimplePlayer->objectName().isEmpty())
            SimplePlayer->setObjectName(QStringLiteral("SimplePlayer"));
        SimplePlayer->resize(1922, 1082);
        SimplePlayer->setMaximumSize(QSize(1922, 1082));
        actionOpenUrl = new QAction(SimplePlayer);
        actionOpenUrl->setObjectName(QStringLiteral("actionOpenUrl"));
        actionStop = new QAction(SimplePlayer);
        actionStop->setObjectName(QStringLiteral("actionStop"));
        actionPause = new QAction(SimplePlayer);
        actionPause->setObjectName(QStringLiteral("actionPause"));
        actionPause->setCheckable(true);
        centralwidget = new QWidget(SimplePlayer);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        centralwidget->setMaximumSize(QSize(1922, 1082));
        gridLayout_2 = new QGridLayout(centralwidget);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        video = new VlcWidgetVideo(centralwidget);
        video->setObjectName(QStringLiteral("video"));
        video->setEnabled(true);
        video->setMaximumSize(QSize(1920, 1080));

        gridLayout_2->addWidget(video, 0, 0, 2, 2);

        SimplePlayer->setCentralWidget(centralwidget);

        retranslateUi(SimplePlayer);

        QMetaObject::connectSlotsByName(SimplePlayer);
    } // setupUi

    void retranslateUi(QMainWindow *SimplePlayer)
    {
        SimplePlayer->setWindowTitle(QApplication::translate("SimplePlayer", "Demo Player", Q_NULLPTR));
        actionOpenUrl->setText(QApplication::translate("SimplePlayer", "Open URL", Q_NULLPTR));
        actionStop->setText(QApplication::translate("SimplePlayer", "Stop", Q_NULLPTR));
        actionPause->setText(QApplication::translate("SimplePlayer", "Pause", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class SimplePlayer: public Ui_SimplePlayer {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SIMPLEPLAYER_H
