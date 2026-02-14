PORTNAME=	python-srsly
DISTVERSION=	2.5.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Modern high-performance serialization utilities for Python.
WWW=		https://pypi.org/project/srsly/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/cython \
		??/py-catalogue@${PY_FLAVOR} \
		??/py-mock@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pytest-timeout@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
