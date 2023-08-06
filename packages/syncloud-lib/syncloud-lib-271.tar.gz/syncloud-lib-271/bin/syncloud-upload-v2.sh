#!/bin/bash -e

if [ -z "$AWS_ACCESS_KEY_ID" ]; then
  echo "AWS_ACCESS_KEY_ID must be set"
  exit 1
fi
if [ -z "$AWS_SECRET_ACCESS_KEY" ]; then
  echo "AWS_SECRET_ACCESS_KEY must be set"
  exit 1
fi

BRANCH=$1
FILE=$2
APP=$(echo "$FILE" | cut -f1 -d_)
VERSION=$(echo "$FILE" | cut -f2 -d_)
ARCH=$(echo "$FILE" | cut -f3 -d_ | cut -f1 -d.)
BUCKET=apps.syncloud.org

if [ "${BRANCH}" == "master" ] || [ "${BRANCH}" == "stable" ] ; then

  sha384sum $FILE | awk '{ print $1 }' > $FILE.sha384
  stat --printf="%s" $FILE > $FILE.size

  s3cmd put $FILE s3://${BUCKET}/apps/$FILE
  s3cmd put $FILE.sha384 s3://${BUCKET}/apps/$FILE.sha384
  s3cmd put $FILE.size s3://${BUCKET}/apps/$FILE.size

  if [ "${BRANCH}" == "stable" ]; then
    BRANCH=rc
  fi

  printf "$VERSION" > version
  s3cmd put version s3://${BUCKET}/releases/${BRANCH}/${APP}.${ARCH}.version

fi
