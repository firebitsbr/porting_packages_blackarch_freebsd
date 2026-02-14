PORTNAME=	torpy
DISTVERSION=	60.ebf000c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Pure python Tor client implementation.
WWW=		https://github.com/torpyorg/torpy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cffi@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-pycparser@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
