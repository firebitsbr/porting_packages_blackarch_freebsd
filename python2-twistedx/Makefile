PORTNAME=	python2-twistedx
DISTVERSION=	20.3.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An asynchronous networking framework written in Python.
WWW=		https://pypi.org/project/Twisted/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-attrs@${PY_FLAVOR} \
		??/py-automat@${PY_FLAVOR} \
		??/py-constantly@${PY_FLAVOR} \
		??/py-hyperlink@${PY_FLAVOR} \
		??/py-incremental@${PY_FLAVOR} \
		??/py-pyhamcrest@${PY_FLAVOR} \
		??/py-zope-interface@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
