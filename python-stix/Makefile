PORTNAME=	python-stix
DISTVERSION=	1.2.0.10
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An API for parsing and generating STIX content.
WWW=		https://pypi.org/project/stix/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cybox@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-mixbox@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
