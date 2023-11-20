# retrofit-8mm-movie-camera-V2
ゼンマイ式デジタルカメラユニットの第二弾


# Raspberry Pi zero2 セットアップ
OS:Raspberry Pi OS Bullseye 64bit lite

$ lsb_release -a
No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 11 (bullseye)
Release:        11
Codename:       bullseye

$ getconf LONG_BIT
64



USB SSH化推奨
apt update,upgrade
```sh
sudo apt update && sudo apt upgrade -y
```

pip3をインストール

```sh
sudo apt -y install python3-dev
sudo apt -y install python3-pip
```

picamera2
opencv-pythonをインストール
```sh
pip3 install picamera2
pip3 install opencv-python

sudo apt -y install libgl1-mesa-dev
```

vim をインストール
```sh
sudo apt -y install vim
vim ~/.vimrc
```
```
set number
```
を追記

Raspberry Pi Camera V3をデバイスツリーに追加
```
sudo vim /boot/config.txt
```
```
dtoverlay=imx708
```

を追記
