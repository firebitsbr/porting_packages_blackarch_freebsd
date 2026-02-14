PORTNAME=	mtscan
DISTVERSION=	167.099482e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Mikrotik RouterOS wireless scanner.
WWW=		https://github.com/kkonradpl/mtscan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		devel/git

RUN_DEPENDS=	??/gtk2 \
		??/libssh \
		??/yajl \
		??/zlib \
		net/libpcap \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
