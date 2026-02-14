PORTNAME=	mfsniffer
DISTVERSION=	0.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A python script for capturing unencrypted TSO login credentials.
WWW=		http://packetstormsecurity.com/files/120802/MF-Sniffer-TN3270-Password-Grabber.html

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	archivers/unzip

RUN_DEPENDS=	lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
