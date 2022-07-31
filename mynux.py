

packages = [
    'xorg-server', 'xorg-apps', 'xorg-xinit', 'qtile', 'ttf-hack', 'rofi',
    'conky', 'volumeicon', 'xwallpaper',
    'alacritty', 'ranger',
    'keepassxc',
    # 'libreoffice-still',
    # 'vlc',
    # 'thunderbird',
    'qutebrowser',
    'code',
    'bluez', 'bluez-utils',
    'git',
    # 'chromium',
]

post_install_actions = {
    'bluez': [
        'sudo systemctl start bluetooth',
        'sudo systemctl enable bluetooth',
    ]
}