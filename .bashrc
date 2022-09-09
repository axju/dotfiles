#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='$(date +"%H:%M:%S") \W > '

if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi


#alias ls='ls --color=auto'
alias la='ls -lah'

alias sync="sudo pacman -Syyy"
alias install="sudo pacman -S"
alias update="sudo pacman -Syyu"

alias rand-back='find /usr/share/backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch'

alias venv='[ ! -e "venv" ] && python -m venv venv ; source venv/bin/activate'
alias pull='find . -name .git -print -execdir git pull \;'
alias recorde='ffmpeg -video_size 1920x1080 -framerate 1 -f x11grab -i :0.0+1366,0 -c:v libx264rgb -crf 0 -preset ultrafast -filter:v "setpts=N/TB/30" -r 30 -y ~/records/$(date +"%Y-%m-%d_%H-%M").mkv'

alias githorn='git config user.name "aje-horn" && git config user.email "axel.juraske@tecalemit.de"'
alias gitaxju='git config user.name "axju" && git config user.email "moin@axju.de"'

complete -cf sudo


export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

