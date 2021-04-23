#!/bin/bash

if [ "$1" = "" ];then
	echo "Please specify release version. ./release <version>"
	exit 1
fi

VERSION="$1"

eval "rm -fR fitcalcpro-$VERSION fitcalcpro-$VERSION.tar.gx" &&
eval "cp -r package-files fitcalcpro-$VERSION" &&
eval "tar -czvf fitcalcpro-$VERSION.tar.gx fitcalcpro-$VERSION" &&
eval "cd fitcalcpro-$VERSION" &&
eval "dh_make -e xsafar23@stud.fit.vutbr.cz -c gpl3 -n -s -f ../fitcalcpro-$VERSION.tar.gx" &&
eval "cd .. && cp debian/install fitcalcpro-$VERSION/debian/install" &&
eval "yes | cp -i -f debian/control fitcalcpro-$VERSION/debian/control" && 
eval "cd fitcalcpro-$VERSION && dpkg-buildpackage -rfakeroot -uc -b"

