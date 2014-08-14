#!/bin/bash
# User/group to run as
USER=jburks
GROUP=staff
# Location of app
APPDIR=/Users/jburks/dev/converse/converse-ecomm-api

set -e
LOGFILE=$APPDIR/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
cd $APPDIR
source bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec bin/gunicorn app:app -w $NUM_WORKERS -b 127.0.0.1:8000\
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE