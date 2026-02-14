PORTNAME=	packet-o-matic
DISTVERSION=	1402.2fe05e7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A real time packet processor. Reads the packet from an input module, match the packet using rules and connection tracking information and then send it to a target module.
WWW=		http://www.packet-o-matic.org/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/libtool \
		??/pkg-config \
		??/xmlrpc-c \
		devel/git

RUN_DEPENDS=	??/libexif \
		??/libmicrohttpd \
		??/libnet \
		??/libxml2 \
		??/lua \
		??/uthash \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
