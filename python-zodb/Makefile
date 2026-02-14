PORTNAME=	python-zodb
DISTVERSION=	6.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A native object database for Python.
WWW=		https://pypi.org/project/ZODB/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-btrees@${PY_FLAVOR} \
		??/py-persistent@${PY_FLAVOR} \
		??/py-transaction@${PY_FLAVOR} \
		??/py-zodbpickle@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
