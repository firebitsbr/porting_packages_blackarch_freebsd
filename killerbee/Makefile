PORTNAME=	killerbee
DISTVERSION=	398.748740d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Framework and tools for exploiting ZigBee and IEEE 802.15.4 networks.
WWW=		https://github.com/riverloopsec/killerbee

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cairo@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pyserial@${PY_FLAVOR} \
		??/py-pyusb@${PY_FLAVOR} \
		??/py-rangeparser@${PY_FLAVOR} \
		??/pygtk \
		lang/python \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
