PORTNAME=	python-m2crypto
DISTVERSION=	0.47.0.r5.g03c22aa
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python crypto and SSL toolkit.
WWW=		https://gitlab.com/m2crypto/m2crypto

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		??/swig \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	lang/python \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
