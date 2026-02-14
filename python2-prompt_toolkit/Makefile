PORTNAME=	python2-prompt_toolkit
DISTVERSION=	2.0.10
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Library for building powerful interactive command lines in Python.
WWW=		https://pypi.org/project/prompt_toolkit/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-pygments@${PY_FLAVOR} \
		??/py-wcwidth@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
