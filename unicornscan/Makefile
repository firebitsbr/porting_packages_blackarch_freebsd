PORTNAME=	unicornscan
DISTVERSION=	0.4.43
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Asynchronous, stateless TCP/UDP scanner for scalable, high-speed network reconnaissance. Includes Alicorn web UI for result visualization.
WWW=		https://github.com/robertelee78/unicornscan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/postgresql \
		devel/git

RUN_DEPENDS=	??/libcap \
		??/libltdl \
		??/libmaxminddb \
		??/postgresql-libs \
		net/libdnet \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
