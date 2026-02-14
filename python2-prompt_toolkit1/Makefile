PORTNAME=	python2-prompt_toolkit1
DISTVERSION=	1.0.15
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Library for building powerful interactive command lines in Python.
WWW=		https://pypi.org/project/prompt-toolkit/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-pygments@${PY_FLAVOR} \
		??/py-wcwidth@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
