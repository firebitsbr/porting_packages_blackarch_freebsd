PORTNAME=	python-eth-utils
DISTVERSION=	5.3.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Common utility functions for ethereum codebases.
WWW=		https://pypi.org/project/eth-utils/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cytoolz@${PY_FLAVOR} \
		??/py-eth-hash@${PY_FLAVOR} \
		??/py-eth-typing@${PY_FLAVOR} \
		??/py-toolz@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
