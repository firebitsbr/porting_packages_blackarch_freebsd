PORTNAME=	python2-reportlab
DISTVERSION=	3.5.32
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The Reportlab Toolkit.
WWW=		https://pypi.org/project/reportlab/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/freetype2 \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pip@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
