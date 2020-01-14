#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui {
class Widget;
}
class VlcMedia;
class VlcMediaPlayer;
class VlcInstance;
class VlcWidgetVideo;
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = 0);
    ~Widget();

//private slots:
  //  void openUrl();
  //  void on_abrir_clicked();
   // void on_play_clicked();
    //void on_pause_clicked();
    //void on_stop_clicked();
    //void on_mute_clicked();
    //void on_volumen_valueChanged(int value);

private:
    Ui::Widget *ui;
    VlcMediaPlayer *mMediaPlayer;
    VlcMedia * _media;
    VlcInstance *_instance;
    VlcWidgetVideo * mVideoWidget;
    void openUrl();

};
#endif // WIDGET_H
