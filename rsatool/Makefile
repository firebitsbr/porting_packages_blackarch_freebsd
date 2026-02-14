PORTNAME=	rsatool
DISTVERSION=	33.c7ef31d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool that can be used to calculate RSA and RSA-CRT parameters.
WWW=		https://github.com/ius/rsatool

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-gmpy2@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
