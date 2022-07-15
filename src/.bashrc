#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='[\u@\h \W]\$ '

alias ls='ls --color=auto'

alias sync="sudo pacman -Syyy"
alias install="sudo pacman -S"
alias update="sudo pacman -Syyu"

alias venv='[ ! -e "venv" ] && python -m venv venv ; source venv/bin/activate'
alias pull='find . -name .git -print -execdir git pull \;'

alias githorn='git config user.name "aje-horn" && git config user.email "axel.juraske@tecalemit.de"'
alias gitaxju='git config user.name "axju" && git config user.email "moin@axju.de"'

complete -cf sudo


