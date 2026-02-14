PORTNAME=	pwndora
DISTVERSION=	1.ba7f6e6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Massive IPv4 scanner, find and analyze internet-connected devices in minutes, create your own IoT search engine at home.
WWW=		https://github.com/alechilczenko/pwndora

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-geoip2@${PY_FLAVOR} \
		??/py-loguru@${PY_FLAVOR} \
		??/py-pycountry@${PY_FLAVOR} \
		??/py-pyfiglet@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		??/webtech \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
