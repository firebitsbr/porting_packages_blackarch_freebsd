PORTNAME=	haka
DISTVERSION=	v0.3.0.r222.g37ae3090
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A collection of tool that allows capturing TCP/IP packets and filtering them based on Lua policy files.
WWW=		https://github.com/haka-security/haka

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/doxygen \
		??/iniparser \
		??/swig

RUN_DEPENDS=	??/capstone \
		??/gawk \
		??/geoip \
		??/libedit \
		??/libnetfilter_queue \
		??/lua \
		??/ncurses \
		??/pcre \
		??/rsync \
		??/wireshark-cli \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
