PORTNAME=	python2-pyvex
DISTVERSION=	7.8.9.26
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python interface to libVEX and VEX IR.
WWW=		https://pypi.org/project/pyvex/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-archinfo@${PY_FLAVOR} \
		??/py-bitstring@${PY_FLAVOR} \
		??/py-cffi@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-pycparser@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
