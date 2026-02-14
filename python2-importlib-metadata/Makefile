PORTNAME=	python2-importlib-metadata
DISTVERSION=	2.1.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Read metadata from Python packages.
WWW=		https://pypi.org/project/importlib-metadata/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-configparser@${PY_FLAVOR} \
		??/py-contextlib2@${PY_FLAVOR} \
		??/py-pathlib2@${PY_FLAVOR} \
		??/py-zipp@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
