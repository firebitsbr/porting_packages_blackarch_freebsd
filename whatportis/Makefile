PORTNAME=	whatportis
DISTVERSION=	54.59a1718
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A command to search port names and numbers.
WWW=		https://github.com/ncrocfer/whatportis

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-click@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-tinydb@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
