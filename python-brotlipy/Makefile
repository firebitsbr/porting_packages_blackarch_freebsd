PORTNAME=	python-brotlipy
DISTVERSION=	0.7.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python binding to the Brotli library.
WWW=		https://github.com/python-hyper/brotlipy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/brotli06 \
		??/py-cffi@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/brotli06 \
		??/py-cffi@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
