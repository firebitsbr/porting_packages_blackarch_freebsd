PORTNAME=	python-timezonefinder
DISTVERSION=	6.6.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python package for finding the timezone of any point on Earth (coordinates) offline.
WWW=		https://github.com/jannikmi/timezonefinder

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cffi@${PY_FLAVOR} \
		??/py-flatbuffers@${PY_FLAVOR} \
		??/py-h3@${PY_FLAVOR} \
		??/py-numba@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
