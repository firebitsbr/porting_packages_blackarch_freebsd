PORTNAME=	python-columnar
DISTVERSION=	1.4.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A library for creating columnar output strings using data as input.
WWW=		https://pypi.org/project/${_pkgname}

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-toolz@${PY_FLAVOR} \
		??/py-wcwidth@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
