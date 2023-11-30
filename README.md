# retrofit-8mm-movie-camera-V2
ゼンマイ式デジタルカメラユニットの第二弾


# Raspberry Pi zero2 セットアップ
OS:Raspberry Pi OS Bullseye 64bit lite

```
$ lsb_release -a
No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 11 (bullseye)
Release:        11
Codename:       bullseye

$ getconf LONG_BIT
64
```

## USB SSH 有効化

config.txtに追記
dtoverlay=dwc2

commandline.txtのrootwait とquietの間に[]の中を追記
rootwait [modules-load=dwc2,g_ether] quiet

USB SSH化推奨
## swap無効、

swap確認
```
swapon -s
```
swap領域をゼロに変更
```
sudo vim /etc/dphys-swapfile
```
```
CONF_SWAPSIZE=0
```

もしくは   
スワップを無効化   
```
sudo systemctl stop dphys-swapfile
sudo systemctl disable dphys-swapfile
```
確認
```
sudo systemctl status dphys-swapfile
```

## /tmpのRAM化



## 必要ソフトインストール
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
https://picamera.readthedocs.io/en/release-1.13/fov.html
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
syntax enable
set expandtab
set tabstop=4
set shiftwidth=4
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
