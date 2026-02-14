PORTNAME=	redirectpoison
DISTVERSION=	1.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool to poison a targeted issuer of SIP INVITE requests with 301 (i.e. Moved Permanently) redirection responses.
WWW=		http://www.hackingexposedvoip.com/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/gcc \
		??/make

RUN_DEPENDS=	??/libnet \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
