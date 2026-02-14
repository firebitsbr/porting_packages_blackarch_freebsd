PORTNAME=	gvm-libs
DISTVERSION=	22.22.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Greenbone Vulnerability Management Libraries.
WWW=		https://github.com/greenbone/gvm-libs

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake

RUN_DEPENDS=	??/cjson \
		??/gnutls \
		??/hiredis \
		??/libgcrypt \
		??/libgio-2.0.so \
		??/libglib-2.0.so \
		??/libgpgme.so \
		??/libldap \
		??/libnet \
		??/libssh.so \
		??/libuuid.so \
		??/libxml2.so \
		??/paho-mqtt-c \
		??/zlib \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
