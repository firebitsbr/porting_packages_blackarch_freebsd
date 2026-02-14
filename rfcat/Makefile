PORTNAME=	rfcat
DISTVERSION=	v2.0.1.r5.g07f99bb
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Swiss-army knife of ISM band radio.
WWW=		https://code.google.com/archive/p/rfcat/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/libusb \
		??/py-future@${PY_FLAVOR} \
		??/py-pyusb@${PY_FLAVOR} \
		??/pyside6 \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
