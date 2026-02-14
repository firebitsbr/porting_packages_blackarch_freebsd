PORTNAME=	honeyd
DISTVERSION=	337.a0f3d64
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A small daemon that creates virtual hosts on a network.
WWW=		https://github.com/DataSoft/Honeyd/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/libedit \
		??/libevent \
		??/pcre \
		??/tcl \
		??/zlib \
		lang/python3 \
		net/libdnet \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
