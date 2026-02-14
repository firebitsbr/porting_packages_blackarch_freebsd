PORTNAME=	pyjfuzz
DISTVERSION=	159.578d44c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python JSON Fuzzer.
WWW=		https://github.com/mseclab/PyJFuzz

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-bottle@${PY_FLAVOR} \
		??/py-gitpython@${PY_FLAVOR} \
		??/py-gramfuzz@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-wsgiref@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
