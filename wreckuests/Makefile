PORTNAME=	wreckuests
DISTVERSION=	75.69b6c27
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Yet another one hard-hitting tool to run DDoS attacks with HTTP-flood.
WWW=		https://github.com/JamesJGoodwin/wreckuests

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-netaddr@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
