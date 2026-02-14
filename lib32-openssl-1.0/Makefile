PORTNAME=	lib32-openssl-1.0
DISTVERSION=	${.ver/[a.z]/.${.ver//[0.9.]/}}
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The Open Source toolkit for Secure Sockets Layer and Transport Layer Security.
WWW=		https://www.openssl.org/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/lib32-gcc-libs \
		??/lib32-glibc

RUN_DEPENDS=	??/lib32-glibc \
		??/openssl-1.0


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
