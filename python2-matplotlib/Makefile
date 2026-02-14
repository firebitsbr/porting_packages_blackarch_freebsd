PORTNAME=	python2-matplotlib
DISTVERSION=	2.2.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python plotting package.
WWW=		https://pypi.org/project/matplotlib/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/freetype2 \
		??/libpng \
		??/py-backports.functools_lru_cache@${PY_FLAVOR} \
		??/py-cycler@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-kiwisolver@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-subprocess32@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
