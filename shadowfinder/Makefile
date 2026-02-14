PORTNAME=	shadowfinder
DISTVERSION=	0.6.1.r0.gcccdd8c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Find possible locations of shadows around the world.
WWW=		https://github.com/bellingcat/ShadowFinder

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-basemap@${PY_FLAVOR} \
		??/py-fire@${PY_FLAVOR} \
		??/py-matplotlib@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pandas@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-suncalc@${PY_FLAVOR} \
		??/py-timezonefinder@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
