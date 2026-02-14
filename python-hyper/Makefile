PORTNAME=	python-hyper
DISTVERSION=	0.7.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	HTTP/2 for Python.
WWW=		https://pypi.org/project/hyper/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-brotlipy@${PY_FLAVOR} \
		??/py-h2@${PY_FLAVOR} \
		??/py-hyperframe@${PY_FLAVOR} \
		??/py-rfc3986@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
