PORTNAME=	pyaxmlparser
DISTVERSION=	v0.3.31.r13.g446bf7c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A simple parser to parse Android XML file.
WWW=		https://github.com/appknox/pyaxmlparser

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/flake8 \
		??/py-asn1crypto@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-coverage@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
