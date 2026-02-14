PORTNAME=	python2-argon2_cffi
DISTVERSION=	19.2.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	CFFI-based Argon2 Bindings for Python.
WWW=		https://github.com/hynek/argon2_cffi

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/argon2 \
		??/py-cffi@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
