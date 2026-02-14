PORTNAME=	nodejs-lts-gallium
DISTVERSION=	16.20.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Evented I/O for V8 javascript (LTS release: Gallium).
WWW=		https://nodejs.org/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/procps-ng \
		lang/python

RUN_DEPENDS=	??/brotli \
		??/c-ares \
		??/icu \
		??/libnghttp2 \
		??/libuv \
		??/zlib \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
