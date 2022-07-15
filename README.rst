Some setup notes
================

Base system
-----------
https://linuxiac.com/arch-linux-install/

https://www.howtoforge.com/tutorial/install-arch-linux-on-virtualbox/

::
    
    cfdisk /dev/sda

/dev/sda1: EFI System partition with 512 MB size, FAT32 formatted.

/dev/sda2: Swap partition, 4GB size.

/dev/sda3: Linux partition,

::
    
    mkfs.fat -F32 /dev/sda1
    mkswap /dev/sda2
    swapon /dev/sda2
    mkfs.ext4 /dev/sda3

    pacman -Syy
    mount /dev/sda3 /mnt
    pacstrap /mnt base linux linux-firmware sudo nano dhcpcd openssh

    genfstab -U /mnt >> /mnt/etc/fstab

    arch-chroot /mnt

    passwd

    useradd -m -G wheel axju
    passwd axju
    EDITOR=nano visudo

    systemctl enable dhcpcd
    systemctl enable sshd.service

    pacman -S grub efibootmgr os-prober mtools
    mkdir /boot/efi
    mount /dev/sda1 /boot/efi
    grub-install --target=x86_64-efi --bootloader-id=grub_uefi
    grub-mkconfig -o /boot/grub/grub.cfg


For RPI
-------
https://www.elektronik-kompendium.de/sites/raspberry-pi/2404241.htm

https://medium.com/@ljupce995/setting-up-raspberry-pi-3-model-b-with-archlinux-tutorial-on-linux-machine-bsdtar-update-e9252a33b68e

https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-3

::
    
    pacman -R --noconfirm linux-aarch64 uboot-raspberrypi
    pacman -S --noconfirm linux-rpi


Some config
-----------
::

    ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime
    hwclock --systohc --utc

    nano /etc/locale.gen
    locale-gen
    localectl set-locale LANG=en_US.UTF-8

    nano /etc/hostname
    nano /etc/hosts


Github + Dotfiles
-----------------
https://medium.com/@doc.aicdev/multiple-ssh-keys-for-git-3d165641f50

Install git and clone dotfiles::

    sudo pacman -S git    
    git clone git@github.com:axju/dotfiles.git ~/.dotfiles

Now create all the links::

    python ~/.dotfiles/bin/link.py -vvv
    python ~/.dotfiles/bin/link.py -vvv ~/.dotfiles-privat

Setup github ssh-keys for privat and work::

    ssh-keygen -t ed25519 -C "moin@axju"
    cat ~/.ssh/id_ed25519.pub
    ssh -T git@github.com

AUR Packages (yay)
------------------
::
    
    sudo pacman -S devel???
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -is

qtile
-----
https://github.com/justinesmithies/qtile-x-dotfiles

::

    sudo pacman -S xorg-server xorg-apps xorg-xinit qtile ttf-hack rofi
    sudo pacman -S conky volumeicon xwallpaper

dmenu for dt
~~~~~~~~~~~~
https://gitlab.com/dwt1/dmenu-distrotube
https://gitlab.com/dwt1/dmscripts.git

::

    yay -S dmscripts-git

::
    
    nano /etc/pacman.conf

::

    [dtos-core-repo]
    SigLevel = Required DatabaseOptional
    Server = https://gitlab.com/dwt1/$repo/-/raw/main/$arch

::

    sudo pacman-key --lsign-key C71486C31555B12E
    sudo pacman -S dmenu-distrotube


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

    sudo pacman -S alacritty ranger
    sudo pacman -S keepassxc
    sudo pacman -S libreoffice-still
    sudo pacman -S vlc
    sudo pacman -S thunderbird
    sudo pacman -S qutebrowser

Bluetooth
---------
::

    pacman -S bluez bluez-utils
    sudo systemctl start bluetooth
    sudo systemctl enable bluetooth

::

    bluetoothctl
    [bluetooth]power on
    [bluetooth]scan on
    (Multiple bluetooth devices in your area should appear per line with its MAC address)
    [bluetooth]pair <your-headset-address-as: ##:##:##:##:##:##>
    [your-headset-brand]connect <##:##:##:##:##:##>
    [your-headset-brand]trust <##:##:##:##:##:##>

::

    sudo nano /etc/bluetooth/main.conf

::

    AutoEnable=true


Audio
-----
::
    sudo pacman -S alsa-utils
