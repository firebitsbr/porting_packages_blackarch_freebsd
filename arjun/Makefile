PORTNAME=	arjun
DISTVERSION=	2.2.7.r5.gd1fb995
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	HTTP parameter discovery suite.
WWW=		https://github.com/s0md3v/Arjun

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dicttoxml@${PY_FLAVOR} \
		??/py-ratelimit@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
