PORTNAME=	python2-requests
DISTVERSION=	2.26.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python HTTP for Humans.
WWW=		https://pypi.org/project/requests/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-chardet@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
