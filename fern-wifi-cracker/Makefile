PORTNAME=	fern-wifi-cracker
DISTVERSION=	301.eff2eb7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	WEP, WPA wifi cracker for wireless penetration testing.
WWW=		http://code.google.com/p/fern-wifi-cracker/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/aircrack-ng \
		??/macchanger \
		??/py-pyqt5@${PY_FLAVOR} \
		??/subversion \
		??/xterm \
		lang/python \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
