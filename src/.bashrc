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

complete -cf sudo
