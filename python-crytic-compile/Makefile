PORTNAME=	python-crytic-compile
DISTVERSION=	0.3.11
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Library to help smart contract compilation.
WWW=		https://pypi.org/project/crytic-compile/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cbor2@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pysha3@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
