PORTNAME=	python2-numpy
DISTVERSION=	1.16.6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The fundamental package for array computing with Python.
WWW=		https://pypi.org/project/numpy/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cython2 \
		??/gcc-fortran \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/cblas \
		??/lapack \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
