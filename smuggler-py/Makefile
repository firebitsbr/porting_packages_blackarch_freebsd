PORTNAME=	smuggler-py
DISTVERSION=	v2.0.0.r0.g48df0e7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python tool used to test for HTTP Desync/Request Smuggling attacks.
WWW=		https://github.com/gwen001/pentest-tools/blob/master/smuggler.py

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colored@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
