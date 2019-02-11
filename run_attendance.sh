FULL_PATH=`readlink $0`
SC_PATH=$(cd "$(dirname $FULL_PATH)" ; pwd -P)
/home/seunghoryu/dev/venv/bin/python $SC_PATH/src/kyobo.py
/home/seunghoryu/dev/venv/bin/python $SC_PATH/src/auction.py
/home/seunghoryu/dev/venv/bin/python $SC_PATH/src/gmarket.py
clear

