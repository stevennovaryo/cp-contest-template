#!/bin/sh

continue_or_exit() {
  while true; do
    read -p "Do you want to continue? (Y/n)" yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit; break;;
        * ) echo "Please answer yes or no.";;
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

# initialize
run_cmd "sudo apt-get install -y git"
run_cmd "sudo apt-get install -y gcc"
# ======================

# installing python stuff
installPreCommit() {
  run_cmd "sudo apt-get install -y python3"
  run_cmd "sudo apt-get install -y python-is-python3"
  run_cmd "python -m pip install pre-commit"
  run_cmd "pre-commit install"
}

while true; do
  read -p "Do you want to install precommit? (Y/n) " yn
  case $yn in
      [Yy]* ) installPreCommit; break;;
      [Nn]* ) break;;
      * ) echo "Please answer yes or no.";;
  esac
done
# ======================

# Installing tcframe
installTcframe() {
  run_cmd "git clone https://github.com/ia-toki/tcframe $HOME/tcframe"
  run_cmd "git clone https://github.com/afaji/tcrand $HOME/tcrand"
  run_cmd "cp -r $HOME/tcrand/include/tcrand $HOME/tcframe/include"
  echo "export TCFRAME_HOME=~/tcframe" >> ~/.bashrc
  echo "alias tcframe=\$TCFRAME_HOME/scripts/tcframe" >> ~/.bashrc
  echo "Installation complete! Please reload the windows."
}

while true; do
  read -p "Do you want to install tcframe and tcrand? (Y/n) " yn
  case $yn in
      [Yy]* ) installTcframe; break;;
      [Nn]* ) break;;
      * ) echo "Please answer yes or no.";;
  esac
done
# ======================
