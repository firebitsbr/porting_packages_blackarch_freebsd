PORTNAME=	pmacct
DISTVERSION=	v1.7.6.r1700.g33a67f4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Small set of multi-purpose passive network monitoring tools [NetFlow IPFIX sFlow libpcap BGP BMP IGP Streaming Telemetry].
WWW=		https://github.com/pmacct/pmacct

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/autoconf \
		devel/git

RUN_DEPENDS=	??/geoip \
		??/mariadb \
		??/rabbitmq \
		??/zeromq \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
