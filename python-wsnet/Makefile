PORTNAME=	python-wsnet
DISTVERSION=	0.1.6.r5.g5a94423
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A lightweight protocol implementation to perform TCP and authentication proxying over websockets.
WWW=		https://github.com/skelsec/wsnet

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiohttp@${PY_FLAVOR} \
		??/py-websockets@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
