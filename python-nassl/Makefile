PORTNAME=	python-nassl
DISTVERSION=	5.4.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Experimental Python wrapper for OpenSSL.
WWW=		https://github.com/nabla-c0d3/nassl

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/openssl-1.0 \
		??/py-invoke@${PY_FLAVOR} \
		??/py-pipenv@${PY_FLAVOR} \
		??/zlib \
		devel/py-setuptools@${PY_FLAVOR} \
		security/openssl

RUN_DEPENDS=	lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
