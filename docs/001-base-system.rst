Base system
===========
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

