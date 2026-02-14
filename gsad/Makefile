PORTNAME=	gsad
DISTVERSION=	24.3.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Greenbone Security Assistant HTTP Server - The server talking to the Greenbone Vulnerability Management daemon (gvmd).
WWW=		https://github.com/greenbone/gsad

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/xmltoman

RUN_DEPENDS=	??/gnutls \
		??/gvm-libs \
		??/gvmd \
		??/libgcrypt \
		??/libglib-2.0.so \
		??/libmicrohttpd \
		??/libxml2.so \
		??/zlib


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
