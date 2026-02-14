PORTNAME=	rr
DISTVERSION=	7192.1f6d9a08
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Record and Replay Framework.
WWW=		https://github.com/mozilla/rr

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/gdb \
		devel/git

RUN_DEPENDS=	??/capnproto \
		??/gcc \
		??/lib32-zlib \
		??/libcap \
		??/libcap-ng \
		??/libpfm4 \
		??/man-pages \
		??/py-pexpect@${PY_FLAVOR} \
		??/zlib \
		lang/python3 \
		net/libpcap \
		shells/bash


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
