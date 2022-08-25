#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='[\u@\h \W]\$ '

if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi


alias ls='ls --color=auto'

alias sync="sudo pacman -Syyy"
alias install="sudo pacman -S"
alias update="sudo pacman -Syyu"

alias venv='[ ! -e "venv" ] && python -m venv venv ; source venv/bin/activate'
alias pull='find . -name .git -print -execdir git pull \;'

alias githorn='git config user.name "aje-horn" && git config user.email "axel.juraske@tecalemit.de"'
alias gitaxju='git config user.name "axju" && git config user.email "moin@axju.de"'

complete -cf sudo


export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
