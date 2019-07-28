clear
echo "
  _____    __  __  _____  _      __    __    __  __  
  \_   \/\ \ \/ _\/__   \/_\    / /   / /   /__\/__\ 
   / /\/  \/ /\ \   / /\//_\\\\  / /   / /   /_\ / \// 
/\/ /_/ /\  / _\ \ / / /  _  \/ /___/ /___//__/ _  \ 
\____/\_\ \/  \__/ \/  \_/ \_/\____/\____/\__/\/ \_/                                                   
";
sudo chmod +x onifw

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/onifw"
    BIN_DIR="$PREFIX/bin/"
    BASH_PATH="$PREFIX/bin/bash"
    TERMUX=true

    pkg install -y git python3 python2 perl gcc ruby

else
    INSTALL_DIR="$HOME/.onifw"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false

fi

echo "[*] - Looking for old install...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[!] - onifw is already installed. Do you want to overwrite anyways? [y/N]";
    read ans
    if [ "$ans" = "y" ] || [ "$ans" = "Y"]; then
        if [ "$TERMUX" = true ]; then
            rm -rf "$INSTALL_DIR"
            rm "$BIN_DIR/onifw"
        else
            sudo rm -rf "$INSTALL_DIR"
            sudo rm "$BIN_DIR/onifw"
        fi
    else
        echo "[*] - In order to install this version you must remove the installed one";
        echo "[*] - Installation aborted.";
        exit
    fi
fi

echo "[*] - Cleaning...";
if [ -d "$ETC_DIR/w0bos" ]; then
    echo "$DIR_FOUND_TEXT"
    if [ "$TERMUX" = true ]; then
        rm -rf "$ETC_DIR/w0bos"
    else
        sudo rm -rf "$ETC_DIR/w0bos"
    fi
fi

echo "[*] - Installing...";
echo "";
git clone https://github.com/w0bos/onifw "$INSTALL_DIR"
echo "#!$BASH_PATH
python3 $INSTALL_DIR/oni.py" '${1+"$@"}' > "$INSTALL_DIR/onifw"
chmod +x "$INSTALL_DIR/onifw";
if [ "$TERMUX" = true ]; then
    cp "$INSTALL_DIR/onifw" "$BIN_DIR"
    cp "$INSTALL_DIR/settings.cfg" "$BIN_DIR"
    cp launcher "$BIN_DIR" onifw
else
    sudo cp "$INSTALL_DIR/onifw" "$BIN_DIR"
    sudo cp "$INSTALL_DIR/settings.cfg" "$BIN_DIR"
fi
#rm "$INSTALL_DIR/onifw";

curl https://raw.githubusercontent.com/w0bos/onifw/master/uninstall > uninstall
sudo chmod +x uninstall
mv uninstall "$INSTALL_DIR"

if [ -d "$INSTALL_DIR" ] ;
then
    echo "[*] - onifw successfully installed"
else
    echo "[!] - Installation failed";
    exit
fi
