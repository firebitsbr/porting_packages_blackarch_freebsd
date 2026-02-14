PORTNAME=	python2-mako
DISTVERSION=	1.1.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A super-fast templating language that borrows the best ideas from the existing templating languages.
WWW=		https://pypi.org/project/mako/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beaker@${PY_FLAVOR} \
		??/py-markupsafe@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
