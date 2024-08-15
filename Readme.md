## Работа в Python 3.9.x с БД Firebird v2.5 в Linux(Debian)


`apt-get install libncurses5`

`apt-get install libstdc++5 libncurses5 libtommath1`

`wget -c https://github.com/FirebirdSQL/firebird/releases/download/R2_5_9/FirebirdSS-2.5.9.27139-0.amd64.tar.gz`

`tar -xzvf FirebirdSS-2.5.9.27139-0.amd64.tar.gz`   

`./install.sh`

`ln -s /opt/firebird/lib/libfbclient.so.2.5.9 /usr/lib/libfbclient.so.2.5.1`
