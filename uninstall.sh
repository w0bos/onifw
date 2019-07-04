!/bin/bash
clear
echo "
 ▒█████   ███▄    █  ██▓  █████▒█     █░    █    ██  ███▄    █  ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄       ██▓     ██▓    ▓█████  ██▀███  
▒██▒  ██▒ ██ ▀█   █ ▓██▒▓██   ▒▓█░ █ ░█░    ██  ▓██▒ ██ ▀█   █ ▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄    ▓██▒    ▓██▒    ▓█   ▀ ▓██ ▒ ██▒
▒██░  ██▒▓██  ▀█ ██▒▒██▒▒████ ░▒█░ █ ░█    ▓██  ▒██░▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▒██░    ▒██░    ▒███   ▓██ ░▄█ ▒
▒██   ██░▓██▒  ▐▌██▒░██░░▓█▒  ░░█░ █ ░█    ▓▓█  ░██░▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░    ▒██░    ▒▓█  ▄ ▒██▀▀█▄  
░ ████▓▒░▒██░   ▓██░░██░░▒█░   ░░██▒██▓    ▒▒█████▓ ▒██░   ▓██░░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░██████▒░██████▒░▒████▒░██▓ ▒██▒
░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓   ▒ ░   ░ ▓░▒ ▒     ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
  ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░ ░       ▒ ░ ░     ░░▒░ ░ ░ ░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
░ ░ ░ ▒     ░   ░ ░  ▒ ░ ░ ░     ░   ░      ░░░ ░ ░    ░   ░ ░  ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒     ░ ░     ░ ░      ░     ░░   ░ 
    ░ ░           ░  ░             ░          ░              ░  ░           ░       ░                 ░  ░    ░  ░    ░  ░   ░  ░   ░     
";

echo "[*] - Looking for current install...";

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/onifw"
    BIN_DIR="$PREFIX/bin/"
    BASH_PATH="$PREFIX/bin/bash"
    TERMUX=true

else
    INSTALL_DIR="$HOME/.onifw"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false

fi

if [ "$TERMUX" = true ]; then
    rm -rf "$ETC_DIR/w0bos"
    rm -rf "$INSTALL_DIR"
    rm -rf "$BIN_DIR/onifw"

elif [ "$TERMUX" = false ]; then
    sudo rm -rf "$ETC_DIR/w0bos"
    sudo rm -rf "$INSTALL_DIR"
    sudo rm -rf "$BIN_DIR/onifw"
fi

echo "[*] - onifw was sucessfully uninstalled."