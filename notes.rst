Some setup notes
================

qtile
-----
::
    sudo pacman -S conky volumeicon xwallpaper


Setup Git
---------
https://medium.com/@doc.aicdev/multiple-ssh-keys-for-git-3d165641f50


Audio
-----
::
    sudo pacman -S alsa-utils


Synology
--------
::
    git clone https://aur.archlinux.org/synology-drive.git
    cd synology-drive
    makepkg -is
    mkdir ~/sync/



Tools
-----
::
    sudo pacman -S keepassxc
    sudo pacman -S libreoffice-still
    sudo pacman -S vlc




Therrd Part Package AUR
-----------------------
::
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -is

dmscripts
~~~~~~~~~
https://gitlab.com/dwt1/dmscripts.git

::
    yay -S dmscripts-git