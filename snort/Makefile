PORTNAME=	snort
DISTVERSION=	2.9.20
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A lightweight network intrusion detection system.
WWW=		http://www.snort.org/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/ca-certificates

RUN_DEPENDS=	??/libdaq \
		??/libtirpc \
		??/libutil-linux \
		??/luajit \
		??/pcre \
		??/zlib \
		net/libdnet \
		net/libpcap \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
