PORTNAME=	arpon
DISTVERSION=	3.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A host-based solution to secure the ARP protocol and prevent MITM attacks via ARP spoofing or cache poisoning.
WWW=		https://arpon.sourceforge.net/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		net/libdnet

RUN_DEPENDS=	??/libnet \
		net/libdnet \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
