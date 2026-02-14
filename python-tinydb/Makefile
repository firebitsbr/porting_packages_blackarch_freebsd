PORTNAME=	python-tinydb
DISTVERSION=	4.8.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Lightweight document oriented database optimized for your happiness.
WWW=		https://pypi.org/project/tinydb/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-pytest-cov@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
