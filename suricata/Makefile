PORTNAME=	suricata
DISTVERSION=	6.0.20
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An Open Source Next Generation Intrusion Detection and Prevention Engine.
WWW=		https://suricata.io/download/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/cargo

RUN_DEPENDS=	??/file \
		??/geoip \
		??/jansson \
		??/libcap-ng \
		??/libmaxminddb \
		??/libnet \
		??/libnetfilter_log \
		??/libnetfilter_queue \
		??/libnfnetlink \
		??/libyaml \
		??/lua \
		??/luajit \
		??/nss \
		??/pcre \
		??/py-magic@${PY_FLAVOR} \
		??/zlib \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
