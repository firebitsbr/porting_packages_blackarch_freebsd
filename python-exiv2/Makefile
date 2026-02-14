PORTNAME=	python-exiv2
DISTVERSION=	0.12.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python3 binding to the library exiv2.
WWW=		https://pypi.org/project/py3exiv2/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/boost \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/boost-libs \
		??/exiv2 \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
