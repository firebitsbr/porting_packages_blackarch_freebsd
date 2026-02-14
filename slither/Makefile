PORTNAME=	slither
DISTVERSION=	5136.45983a859
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Solidity static analysis framework written in Python 3.
WWW=		https://github.com/crytic/slither

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-crytic-compile@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-pysha3@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
