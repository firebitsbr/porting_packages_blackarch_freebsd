PORTNAME=	python2-bcrypt
DISTVERSION=	3.1.7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Modern password hashing for your software and your servers.
WWW=		https://pypi.org/project/bcrypt/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cffi@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
