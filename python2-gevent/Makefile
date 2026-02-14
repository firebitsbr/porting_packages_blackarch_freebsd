PORTNAME=	python2-gevent
DISTVERSION=	21.1.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Coroutine-based network library.
WWW=		https://pypi.org/project/gevent/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cython2 \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-greenlet@${PY_FLAVOR} \
		??/py-zope-event@${PY_FLAVOR} \
		??/py-zope-interface@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
