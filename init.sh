#!/bin/sh

continue_or_exit() {
  while true; do
    read -p "Do you want to continue? (Y/n)" yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit; break;;
        * ) ;;
    esac
  done
}

run_cmd() {
  local command="$@"
  if $command 2>&1 >/dev/null; then
    echo "\e[32m[SUCCESS]\e[0m $command"
    return 0
  else
    echo "\e[31m[FAILED]\e[0m $command"
    echo "Canceling the process..."
    echo "Running the command again in non-silent mode"
    $command
    continue_or_exit
    return 1
  fi
}

# Install Git and GCC
run_cmd "sudo apt-get install -y git"
run_cmd "sudo apt-get install -y gcc"
# ======================

# Install Python and Pre-commit
installPreCommit() {
  run_cmd "sudo apt-get install -y python3"
  run_cmd "sudo apt-get install -y python-is-python3"
  run_cmd "python -m pip install pre-commit"
  run_cmd "pre-commit install"
}

while true; do
  read -p "Do you want to download and install Python and pre-commit? (Y/n) " yn
  case $yn in
      [Yy]* ) installPreCommit; break;;
      [Nn]* ) break;;
      * ) ;;
  esac
done
# ======================

# Installing tcframe and tcrand

need_reload=0

installTcframe() {
  run_cmd "git clone https://github.com/ia-toki/tcframe $HOME/tcframe"
  echo "export TCFRAME_HOME=~/tcframe" >> ~/.bashrc
  echo "alias tcframe=\$TCFRAME_HOME/scripts/tcframe" >> ~/.bashrc
  need_reload=1
}

while true; do
  read -p "Do you want to download and install tcframe? (Y/n) " yn
  case $yn in
      [Yy]* ) installTcframe; break;;
      [Nn]* ) break;;
      * ) ;;
  esac
done

installTcrand() {
  run_cmd "git clone https://github.com/afaji/tcrand $HOME/tcrand"
  run_cmd "cp -r $HOME/tcrand/include/tcrand $HOME/tcframe/include"
}

while true; do
  read -p "Do you want to download and install tcrand? (Y/n) " yn
  case $yn in
      [Yy]* ) installTcrand; break;;
      [Nn]* ) break;;
      * ) ;;
  esac
done

if [ $need_reload -eq 1 ]
then
  echo "Installation complete! Please reload the terminal session."
else
  echo "Installation complete!"
fi
# ======================
