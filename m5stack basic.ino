#include <M5Stack.h>
#include <WiFi.h>
#include <WiFiUdp.h>
#include <WiFiUDP.h>
#include "AudioFileSourceSD.h"
#include "AudioFileSourceID3.h"
#include "AudioGeneratorMP3.h"
#include "AudioOutputI2S.h"

#define N 1024

AudioGeneratorMP3 *mp3;
AudioFileSourceSD *file;
AudioOutputI2S *out;
AudioFileSourceID3 *id3;

/* The udp library class*/
WiFiUDP udp;

/*接続設定*/
const char* ssid     = "libAndroid2F";
const char* password = "iiLibraKokoro";
const int my_port = 50008;
const int pc_port = 50007; //送信先のポート
const char* address = "192.168.11.11" ;

/* fixed IP address */
IPAddress ip(192,168,11,129);
IPAddress gateway(192,168,233,1);
IPAddress subnet(255,255,255,0);
IPAddress DNS(160,247,5,110);

/*ロボット側PCからの文字列*/
String Str1 = "call1";//判定
String Str2 = "call2";
String Str3 = "call3";
String message;//PCからの受取
int cnt;
bool push = false;
int packetSize;
char packetBuffer[N];

/*音量*/

int vol = 1;//音量
bool nowCall = false;
int callCnt = 3;


/*Wi-Fi*/
void print_wifi_state() {
  M5.Lcd.clear(BLACK);  // clear LCD
  M5.Lcd.setTextColor(YELLOW);
  M5.Lcd.setCursor(3, 100);
  M5.Lcd.println("");
  M5.Lcd.println("WiFi connected.");
  M5.Lcd.print("IP address: ");
  M5.Lcd.println(WiFi.localIP());
  M5.Lcd.print("Port: ");
  M5.Lcd.println(my_port);
}

void setup_wifi() {
  M5.Lcd.setTextColor(RED);
  M5.Lcd.setTextSize(2);
  M5.Lcd.setCursor(3, 100);
  M5.Lcd.print("Connecting to ");
  M5.Lcd.println(ssid);

  // setup wifi
  WiFi.mode(WIFI_STA);  // WIFI_AP, WIFI_STA, WIFI_AP_STA or WIFI_OFF

  WiFi.config(ip, gateway, subnet, DNS);
  delay(10);
  
  WiFi.begin(ssid, password);
  // WiFi.begin();

  // Connecting ..
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    M5.Lcd.print(".");
  }

  // print state
  print_wifi_state();

  udp.begin(my_port);
}



/*バッテリー表示*/
static int giBattery = 0;
static int giBatteryOld = 0xFF;

void battery (int b) {
  if ( giBatteryOld != b )
  {
    // 電池へそ
    M5.Lcd.fillRoundRect(307, 20, 6, 12, 1, WHITE);
    // 大外枠
    M5.Lcd.fillRoundRect(257, 14, 50, 26, 1, WHITE);

    // 90%以上
    if ( b >= 90  )
    {
      M5.Lcd.fillRect(294, 16, 10, 23, GREEN);
    }
    // 75%以上
    if ( b > 70  )
    {
      M5.Lcd.fillRect(283, 16, 10, 23, GREEN);
    }
    // 50%以上
    if ( b >= 50  )
    {
      M5.Lcd.fillRect(272, 16, 10, 23, GREEN);
    }
    // 25%以上
    if ( b >= 25 )
    {
      M5.Lcd.fillRect(261, 16, 10, 23, GREEN);
    }
    if (b <= 25)
    {
      M5.Lcd.fillRect(261, 16, 10, 23, RED);
    }
  }
  // 前回値更新
  giBatteryOld = b;
}



//sound files
void playMP3(char *filename) {
  file = new AudioFileSourceSD(filename);
  id3 = new AudioFileSourceID3(file);
  out = new AudioOutputI2S(0, 1); // Output to builtInDAC
  out->SetOutputModeMono(true);
  out->SetGain(1.0);
  mp3 = new AudioGeneratorMP3();
  mp3->begin(id3, out);
  while (mp3->isRunning()) {
    if (!mp3->loop()) mp3->stop();
  }
}


/*音量調節*/
//スピーカーアイコン
void volumeMark(int vol) {

  M5.Lcd.fillRect(260, 200, 10, 20, WHITE);
  M5.Lcd.fillTriangle(260, 210, 280, 190, 280, 230, WHITE);

  if (vol > 0) {
    M5.Lcd.fillRect(285, 205, 5, 10, WHITE);
  }
  if (vol > 1) {
    M5.Lcd.fillRect(295, 200, 5, 20, WHITE);
  }
  if (vol > 2) {
    M5.Lcd.fillRect(305, 190, 5, 40, WHITE);
  }
}



/* task0のループ関数 */
void task0(void* arg) {
  while (1) {
    char packetBuffer[N];
    int packetSize = udp.parsePacket();

    // get packet

    if (packetSize) {//メッセージを受け取ったら
      int len = udp.read(packetBuffer, packetSize);
      // message = packetBuffer;
      // push = false;
      // if (len > 0) {
      //   packetBuffer[len] = '\0'; // end
      // }
      // M5.Lcd.clear(BLACK);

      //アイコンの再表示
      giBattery = N;
      battery(giBattery);

      // print and sound

      // if (message.equals(Str1))//call1が送られたら
      // {
      //   nowCall = true;
      //   callCnt = 3;

        M5.Lcd.setTextColor(GREEN);
        M5.Lcd.setCursor(10, 120);
        M5.Lcd.setTextSize(4);
        M5.Lcd.println("Certificate");

        while ( push == false) {
          if (vol != 0) {
            playMP3("/c1.mp3");
            callCnt--;
          } else {
            break;
          }
          if (callCnt == 0) {
            break;
          }
          delay(1);
        }
      }
    //   else if (message.equals(Str2))//call2
    //   {
    //     nowCall = true;
        
    //     M5.Lcd.setTextColor(BLUE);
    //     M5.Lcd.setCursor(20, 100);
    //     M5.Lcd.setTextSize(4);
    //     M5.Lcd.println("Copy");

    //     while ( push == false) {
    //       if (vol != 0) {
    //         playMP3("/c1.mp3");
    //       } else {
    //         break;
    //       }
    //       if (callCnt == 0) {
    //         break;
    //       }
    //       delay(1);
    //     }
    //   }
    //   else if (message.equals(Str3))//call3
    //   {
    //     nowCall = true;

    //     M5.Lcd.setTextColor(RED);
    //     M5.Lcd.setCursor(60, 100);
    //     M5.Lcd.setTextSize(6);
    //     M5.Lcd.println(packetBuffer);

    //     while ( push == false) {
    //       if (vol != 0) {
    //         playMP3("/c1.mp3");
    //       } else {
    //         break;
    //       }
    //       if (callCnt == 0) {
    //         break;
    //       }
    //       delay(1);
    //     }
    //   }
    // }
  }

  delay(1);
}




void setup() {
  M5.begin();
  M5.Lcd.clear(WHITE);

  // setup wifi
  setup_wifi();

  // //task0のループ関数を起動
  // xTaskCreatePinnedToCore(task0, "Task0", 4096, NULL, 1, NULL, 1);
  // udp.begin(my_port);
  // M5.Power.begin();
  // if (!M5.Power.canControl()) {
  //   //can't control.
  //   M5.Lcd.print("NG");
  //   return;
  // }

  M5.Lcd.clear(BLACK);
}

void loop() {
  M5.update();              //M5Stackの内部処理を更新
  M5.Speaker.update();


  /*PCへの送信*/
  // if (M5.BtnA.wasPressed()) {
  //   if (nowCall) {
  //     push = true;
  //     nowCall = false;
  //     udp.beginPacket(address, pc_port);
  //     udp.write('t');
  //     udp.write('r');
  //     udp.write('u');
  //     udp.write('e');
  //     udp.endPacket();

  //     M5.Speaker.mute();
  //     M5.Lcd.clear(BLACK);

  //     //アイコンの再表示
  //     giBattery = N;
  //     battery(giBattery);
  //   }
  // }
  /*音量*/
  char packetBuffer[N];
  int packetSize = udp.parsePacket();
  callCnt=3;


    // get packet

  if (packetSize!=0) {//メッセージを受け取ったら
    int len = udp.read(packetBuffer, packetSize);
      M5.Lcd.setTextColor(GREEN);
      M5.Lcd.setCursor(10, 120);
      M5.Lcd.setTextSize(4);
      M5.Lcd.println("Certificate");
      playMP3("/c1.mp3");
      packetSize=0;
      M5.Lcd.clear(BLACK);

      }
      
  

  if (M5.BtnC.wasPressed()) {
    vol ++;
    if (vol >= 4) {
      vol = 0;
      M5.Lcd.clear(BLACK);

      //アイコンの再表示
      giBattery = N;
      battery(giBattery);
    }
  }

  //アイコン表示
  M5.Speaker.setVolume(vol * 3);
  volumeMark(vol);

  giBattery = M5.Power.getBatteryLevel();
  battery(giBattery);



  delay(1);
}