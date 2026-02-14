PORTNAME=	wi-feye
DISTVERSION=	1.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An automated wireless penetration testing tool written in python, its designed to simplify common attacks that can be performed on wifi networks so that they can be executed quickly and easily.
WWW=		http://wi-feye.za1d.com/download.php

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/aircrack-ng \
		??/driftnet \
		??/dsniff \
		??/ettercap \
		??/evilgrade \
		??/hamster \
		??/py-colorama@${PY_FLAVOR} \
		??/py-pexpect@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
