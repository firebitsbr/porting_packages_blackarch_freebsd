PORTNAME=	ndpi
DISTVERSION=	4.14
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Open and Extensible GPLv3 Deep Packet Inspection Library.
WWW=		https://github.com/ntop/nDPI

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/json-c \
		??/libmaxminddb \
		??/numactl \
		??/pcre2 \
		??/rrdtool \
		net/libpcap

RUN_DEPENDS=	net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
