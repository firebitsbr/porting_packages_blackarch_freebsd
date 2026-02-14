PORTNAME=	python-python-dxf
DISTVERSION=	12.1.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Package for accessing a Docker v2 registry.
WWW=		https://pypi.org/project/python-dxf/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-jwcrypto@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-www-authenticate@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
