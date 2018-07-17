FULL_PATH=`readlink $0`
SC_PATH=$(cd "$(dirname $FULL_PATH)" ; pwd -P)
python $SC_PATH/src/kyobo.py
python $SC_PATH/src/auction.py

