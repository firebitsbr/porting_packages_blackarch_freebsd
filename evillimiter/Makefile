PORTNAME=	evillimiter
DISTVERSION=	36.46d2033
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool that limits bandwidth of devices on the same network without access.
WWW=		https://github.com/bitbrute/evillimiter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-terminaltables@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/scapy \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
