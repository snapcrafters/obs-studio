#!/bin/bash
FOLDER=https://ppa.launchpadcontent.net/obsproject/obs-studio/ubuntu/pool/main/o/obs-studio/
DISTRO_CODE=noble
DEB_URL=${FOLDER}$(curl -s "${FOLDER}" | grep "${DISTRO_CODE}" | grep -oP 'href="[^"]+\.deb"' | cut -d'"' -f2 | sort -V | tail -n 1)
VERSION="$(basename "$DEB_URL" | sed -E 's/^[^_]+_([0-9]+\.[0-9]+\.[0-9]+)-.*$/\1/')"
if [ "$1" = "version" ]; then
	echo $VERSION
else
	echo $DEB_URL
fi
