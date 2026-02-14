PORTNAME=	python2-google-api-python-client
DISTVERSION=	1.7.11
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Google API Client Library for Python.
WWW=		https://pypi.org/project/google-api-python-client/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-google-auth-httplib2@${PY_FLAVOR} \
		??/py-uritemplate@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
