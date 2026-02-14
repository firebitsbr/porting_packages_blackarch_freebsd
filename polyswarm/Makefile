PORTNAME=	polyswarm
DISTVERSION=	3.16.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An interface to the public and private PolySwarm APIs.
WWW=		https://github.com/polyswarm/polyswarm-api

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-virtualenv@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
