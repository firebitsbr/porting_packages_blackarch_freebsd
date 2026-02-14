PORTNAME=	python2-pep517
DISTVERSION=	0.11.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Wrappers to build Python packages using PEP 517 hooks.
WWW=		https://pypi.org/project/pep517/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-importlib-metadata@${PY_FLAVOR} \
		??/py-pytoml@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
