PORTNAME=	python2-scipy
DISTVERSION=	1.2.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Scientific Library for Python.
WWW=		https://pypi.org/project/scipy/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/gcc-fortran \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-numpy@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
