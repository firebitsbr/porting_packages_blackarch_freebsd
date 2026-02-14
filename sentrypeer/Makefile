PORTNAME=	sentrypeer
DISTVERSION=	v3.0.0.r14.g02173c8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Protect SIP Servers from bad actors.
WWW=		https://github.com/SentryPeer/SentryPeer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/autoconf-archive \
		??/cmocka \
		devel/git

RUN_DEPENDS=	??/fmt \
		??/http-parser \
		??/jansson \
		??/libmicrohttpd \
		??/libosip2 \
		??/opendht-c \
		??/pcre2 \
		??/sqlite \
		??/uuid \
		ftp/curl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
