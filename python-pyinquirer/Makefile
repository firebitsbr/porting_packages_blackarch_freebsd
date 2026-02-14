PORTNAME=	python-pyinquirer
DISTVERSION=	1.0.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python module for common interactive command line user interfaces.
WWW=		https://github.com/CITGuru/PyInquirer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-regex@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
