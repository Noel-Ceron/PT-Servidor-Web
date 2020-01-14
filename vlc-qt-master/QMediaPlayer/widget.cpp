#include "widget.h"
#include "ui_widget.h"
#include <QMediaPlayer>
#include <QObject>
#include <QVideoWidget>
#include <QFileDialog>
#include <QMainWindow>

#include <VLCQtCore/Common.h>
#include <VLCQtCore/Instance.h>
#include <VLCQtCore/Media.h>
#include <VLCQtCore/MediaPlayer.h>
#include <VLCQtWidgets/WidgetVideo.h>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget),
    _media(0)
{
    ui->setupUi(this);
    _instance = new VlcInstance(VlcCommon::args(), this);
    mMediaPlayer = new VlcMediaPlayer(_instance);
    mVideoWidget = new VlcWidgetVideo(this);
    mMediaPlayer->setVideoWidget(mVideoWidget);
    mVideoWidget->setMediaPlayer(mMediaPlayer);
    //ui->videoLayout->setMediaPlayer(mMediaPlayer);
    ui->videoLayout->addWidget(mVideoWidget);

}

Widget::~Widget()
{
    delete mMediaPlayer;
    delete _media;
    delete _instance;
    delete ui;
    }

void Widget:: openUrl()
{
    //OpenFileName(this, tr("Open file"));
    QString url = "rtmp://streaming.upiita.ipn.mx/difusion.upiita/difusion";
    _media= new VlcMedia(url, true, _instance);
    mMediaPlayer->open(_media);
}




  //  connect(mMediaPlayer, &QMediaPlayer::positionChanged, [&] (qint64 pos){
    //    ui->avance->setValue(pos);
    //});
    //connect(mMediaPlayer,&QMediaPlayer::durationChanged, [&] (qint64 dur){
      //  ui->avance->setMaximum(dur);
    //});


//}

//Widget::~Widget()
//{
  //  delete ui;
//}



