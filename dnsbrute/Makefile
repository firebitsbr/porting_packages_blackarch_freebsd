PORTNAME=	dnsbrute
DISTVERSION=	2.b1dc84a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Multi-theaded DNS bruteforcing, average speed 80 lookups/second with 40 threads.
WWW=		https://github.com/d4rkcat/dnsbrute

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
