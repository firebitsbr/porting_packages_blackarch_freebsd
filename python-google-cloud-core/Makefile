PORTNAME=	python-google-cloud-core
DISTVERSION=	2.5.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Google Cloud API client core library.
WWW=		https://pypi.org/project/google-cloud-core/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-google-api-core@${PY_FLAVOR} \
		??/py-google-auth@${PY_FLAVOR} \
		??/py-importlib-metadata@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
