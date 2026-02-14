PORTNAME=	openvas-scanner
DISTVERSION=	23.17.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OpenVAS Scanner of the Greenbone Community Edition.
WWW=		https://github.com/greenbone/openvas-scanner

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/doxygen \
		??/graphviz \
		??/inetutils \
		devel/cargo

RUN_DEPENDS=	??/gvm-libs \
		??/json-glib \
		??/libbsd \
		??/libgcrypt \
		??/net-snmp \
		??/redis \
		??/rsync


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
