#!/usr/bin/env bash

#CHITOSE_FRIST_START_CHECK="CHITOSE_FIRST_START"
#
#if [ ! -f $CHITOSE_FIRST_START_CHECK ]; then
#  touch $CHITOSE_FIRST_START_CHECK
#  echo 'DO NOT EDIT THIS FILE! THIS IS USED WHEN YOU FIRST RUN CHITOSE USING DOCKER!' >> $CHITOSE_FIRST_START_CHECK
#  prisma db push --schema chitose/schema.prisma
#fi

prisma db push --schema /Chitose/schema.prisma
exec uvicorn main:app --port 8000 --host 0.0.0.0