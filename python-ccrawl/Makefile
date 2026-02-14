PORTNAME=	python-ccrawl
DISTVERSION=	1.9
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Uses clang to build a database related to various C/C++ data structures.
WWW=		https://github.com/bdcht/ccrawl

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/clang \
		??/py-click@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		??/py-tinydb@${PY_FLAVOR} \
		??/py-traitlets@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
