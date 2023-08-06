#!/bin/bash -e

if [ -z "$AWS_ACCESS_KEY_ID" ]; then
  echo "AWS_ACCESS_KEY_ID must be set"
  exit 1
fi
if [ -z "$AWS_SECRET_ACCESS_KEY" ]; then
  echo "AWS_SECRET_ACCESS_KEY must be set"
  exit 1
fi

APP=$1
ARCH=$2
BUCKET=apps.syncloud.org

s3cmd cp s3://${BUCKET}/releases/rc/${APP}.${ARCH}.version s3://${BUCKET}/releases/stable/${APP}.${ARCH}.version