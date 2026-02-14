PORTNAME=	rfcrack
DISTVERSION=	128.db73830
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Software Defined Radio Attack Tool.
WWW=		https://github.com/cclabsInc/RFCrack

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-bitstring@${PY_FLAVOR} \
		??/py-libusb@${PY_FLAVOR} \
		??/py-matplotlib@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pyusb@${PY_FLAVOR} \
		??/rfcat \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
