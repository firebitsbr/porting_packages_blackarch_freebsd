PORTNAME=	btlejack
DISTVERSION=	v2.1.1.r1.gc487859
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Bluetooth Low Energy Swiss-army knife.
WWW=		https://github.com/virtualabs/btlejack

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-halo@${PY_FLAVOR} \
		??/py-pyserial@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
