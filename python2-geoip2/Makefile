PORTNAME=	python2-geoip2
DISTVERSION=	3.0.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	MaxMind GeoIP2 API.
WWW=		https://pypi.python.org/pypi/GeoIP/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/geoip \
		??/py-maxminddb@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
