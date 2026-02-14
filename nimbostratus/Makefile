PORTNAME=	nimbostratus
DISTVERSION=	54.c7c206f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tools for fingerprintinging and exploiting Amazon cloud infrastructures.
WWW=		https://github.com/andresriancho/nimbostratus

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-boto@${PY_FLAVOR} \
		??/py-httpretty@${PY_FLAVOR} \
		??/py-nose@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
