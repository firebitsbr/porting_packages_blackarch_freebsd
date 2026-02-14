PORTNAME=	python-google-cloud-logging
DISTVERSION=	3.13.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Stackdriver Logging API client library.
WWW=		https://pypi.org/project/google-cloud-logging/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-google-api-core@${PY_FLAVOR} \
		??/py-google-cloud-core@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
