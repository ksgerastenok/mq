@echo off

set QMGR=%1
set PORT=%2

endmqm -w %QMGR%
dltmqm %QMGR%
crtmqm -p %PORT% %QMGR%
amqmdain reg %QMGR% -c add -s Log -v LogType=CIRCULAR
amqmdain reg %QMGR% -c add -s Log -v LogFilePages=16384
amqmdain reg %QMGR% -c add -s Log -v LogPrimaryFiles=8
amqmdain reg %QMGR% -c add -s Log -v LogSecondaryFiles=4
amqmdain reg %QMGR% -c add -s Log -v LogWriteIntegrity=TripleWrite
amqmdain reg %QMGR% -c add -s SSL -v AllowSSLV3=Y
amqmdain reg %QMGR% -c add -s SSL -v AllowTLSV1=Y
amqmdain reg %QMGR% -c add -s SSL -v AllowWeakCipherSpec=ALL
amqmdain reg %QMGR% -c add -s SSL -v OCSPAuthentication=OPTIONAL
amqmdain reg %QMGR% -c add -s SSL -v OCSPCheckExtensions=NO
amqmdain reg %QMGR% -c add -s TCP -v KeepAlive=YES
amqmdain reg %QMGR% -c add -s Channels -v MaxChannels=5000
amqmdain reg %QMGR% -c add -s Channels -v PasswordProtection=OPTIONAL
amqmdain auto %QMGR%
strmqm %QMGR%

type ./create.mqsc | runmqsc %QMGR% > ./report.txt
