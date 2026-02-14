PORTNAME=	wifiscanmap
DISTVERSION=	135.9adcd08
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Another wifi mapping tool.
WWW=		https://github.com/mehdilauters/wifiScanMap

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/aircrack-ng \
		??/bluez \
		??/bower \
		??/gpsd \
		??/py-gps@${PY_FLAVOR} \
		??/py-pysqlite@${PY_FLAVOR} \
		??/py-rpi-gpio@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
