PORTNAME=	chameleonmini
DISTVERSION=	613.ad0eece
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Official repository of ChameleonMini, a freely programmable, portable tool for NFC security analysis that can emulate and clone contactless cards, read RFID tags and sniff/log RF data.
WWW=		https://github.com/emsec/ChameleonMini

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/avr-gcc \
		??/avr-libc \
		devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-pyserial@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
