PORTNAME=	haystack
DISTVERSION=	1823.c178b5a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python framework for finding C structures from process memory - heap analysis - Memory structures forensics.
WWW=		https://github.com/trolldbois/python-haystack

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-levenshtein@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-ptrace@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
