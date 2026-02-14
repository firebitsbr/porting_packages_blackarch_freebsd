PORTNAME=	ubertooth
DISTVERSION=	2020.12.R1.r33.ge0fd34d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A 2.4 GHz wireless development board suitable for Bluetooth experimentation. Open source hardware and software. Tools only.
WWW=		https://github.com/greatscottgadgets/ubertooth

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/libbtbb \
		??/libusb \
		??/py-libusb1@${PY_FLAVOR} \
		??/py-qtpy@${PY_FLAVOR} \
		lang/python \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
