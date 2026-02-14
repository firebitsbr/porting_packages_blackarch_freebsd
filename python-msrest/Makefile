PORTNAME=	python-msrest
DISTVERSION=	0.7.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	AutoRest swagger generator Python client runtime.
WWW=		https://pypi.org/project/msrest/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-isodate@${PY_FLAVOR} \
		??/py-requests-oauthlib@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
