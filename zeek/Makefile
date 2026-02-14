PORTNAME=	zeek
DISTVERSION=	v8.2.0.dev.r183.g875bdcb
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A powerful network analysis framework that is much different from the typical IDS you may know.
WWW=		https://github.com/zeek/zeek

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/bison \
		??/cmake \
		??/flex \
		??/swig \
		??/zeromq \
		??/zlib \
		devel/git \
		lang/python \
		www/node

RUN_DEPENDS=	??/crypto++ \
		??/openssl-1.0 \
		??/perl \
		??/swig \
		lang/python \
		lang/ruby \
		net/libpcap \
		shells/bash


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
