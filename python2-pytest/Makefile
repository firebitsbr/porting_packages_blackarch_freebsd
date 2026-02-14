PORTNAME=	python2-pytest
DISTVERSION=	4.6.11
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Simple powerful testing with Python.
WWW=		https://pypi.org/project/pytest/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-pip@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-atomicwrites@${PY_FLAVOR} \
		??/py-attrs@${PY_FLAVOR} \
		??/py-importlib-metadata@${PY_FLAVOR} \
		??/py-more-itertools@${PY_FLAVOR} \
		??/py-py@${PY_FLAVOR} \
		??/py-wcwidth@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
