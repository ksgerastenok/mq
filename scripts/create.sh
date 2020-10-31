#!/usr/bin/sh

#QMGR=SB.ESBGW.FI.IN.GW1
QMGR=${1}
PORT=${2}

endmqm -w ${QMGR}
dltmqm ${QMGR}
crtmqm -p ${PORT} ${QMGR}
strmqm ${QMGR}

cat ./create.mqsc | runmqsc ${QMGR} > ./create.txt
