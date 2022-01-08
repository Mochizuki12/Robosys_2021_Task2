# Robosys_2021_Task2

---

# １．概要
2021年度ロボットシステム学の課題で作成したROSパッケージです．

サーボモータ二つを使用して、加速度・ジャイロセンサの動きに対して、2軸で姿勢を水平に保つことができます．


---

# ２．確認済み動作環境

- Raspberry Pi4 Model B 8GB OKdo版

- OS : Ubuntu 20.04

- ROS Noetic


---

# ３．用意する物

- SG90 9g Micro Servo × 2

- ジャンパー線（オス-メス）× 8

- ジャンパー線（オス-オス）× 13

- GY-521 (MPU6050) × 1

- ブレッドボード × 1

- Raspberry Pi4 Model B × 1


---

# ４．実体配線図

下の図のように配線してください．

![7seg_ブレッドボード](https://user-images.githubusercontent.com/92071009/146275109-d0719f07-5a0c-4839-9b98-1e867ac421b9.png)

---

# ５．Raspberry Pi側の準備

pigpio,i2c-tools,python3-smbusがインストール済みの場合は、**５．mpu6050-raspberryのインストール**から行ってください．


#### 5.1.unzipのインストール

```
$ sudo apt install unzip
```

#### 5.2.pigpioのインストール

以下のコマンドを上から順に実行してください。

```
$ wget https://github.com/joan2937/pigpio/archive/master.zip
$ unzip master.zip
$ cd pigpio-master
$ make
$ sudo make install
```
>　参考サイト：pigpio library  
>　http://abyz.me.uk/rpi/pigpio/download.html


#### 5.3.i2c-toolsのインストール

```
$ sudo apt install i2c-tools
```

#### 5.4.Python3-sumbusのインストール

```
sudo apt install python3-smbus
```

#### 5.5.mpu6050-raspberryのインストール

```
pip install mpu6050-raspberrypi
```

必要かわかりませんが、以下のコマンドを上から順に実行して、777で権限をつけます．

```
$ cd .local/lib/python3.8/site-packages/mpu6050
$ chmod 777 mpu6050.py
$ chmod 777 __init__.py
```

#### 5.6.センサが認識されているかを確認

以下のコマンドを実行し確認する．

```
$ sudo i2cdetect -y 1
```

下のような表示がされたら認識されている

```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- 68 -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

#### 5.7.IMU,i2cの設定

以下のコマンドを上から順に実行してください

```
$ sudo gpasswd -a $USER gpio
$ sudo adduser $USER gpio
$ sudo adduser $USER i2c
$ sudo chmod 777 /dev/ttyAMA0
```

>　参考サイト：趣味開発、実装をまとめるブログ  
>　https://www.takeshi-1222.com/entry/raspi-ros2-imu


---

# ６パッケージのインストールと使用方法

## 6.1.本パッケージのインストール

パッケージをROSのworkspaceのsrcフォルダで以下のコマンドを上から順に実行してください．

```
$ git clone 

$ cd ../

$ catkin_make
```


## 6.2.使用方法


---

# ６．デモ動画
上記の手順を踏み実際に動作させた動画です．動画ではわかりやすいように使用例として、他の部品を使っています．

[ROSを使用した相補フィルタのスタビライザ](https://youtu.be/__I8KDhq_y0)

---

# ７．参考サイト

相補フィルタを実装するために以下のサイトを参考にしました．

> imo.Lab 加速度センサーから軸廻り角度への変換計算  
> https://garchiving.com/angle-from-acceleration/


> 即戦力モノづくり!エンジニアへの道標 相補フィルタのしくみを解明してみる【加速度・ジャイロセンサ】 
> https://depfields.com/complementary-filter/

---

# ８．使用した外部ライブラリ

> mpu6050  
> https://github.com/m-rtijn/mpu6050.git

> pigpio  
> http://abyz.me.uk/rpi/pigpio/index.html

---

# ９．ライセンス

[BSD 3-Clause "New" or "Revised" License](https://github.com/Mochizuki12/Robosys2021_Task1/blob/main/COPYING)
