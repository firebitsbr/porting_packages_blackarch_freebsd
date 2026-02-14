PORTNAME=	darkarmour
DISTVERSION=	4.f10228a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Store and execute an encrypted windows binary from inside memory, without a single bit touching disk.
WWW=		https://github.com/bats3c/darkarmour

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/mingw-w64-binutils \
		??/mingw-w64-crt \
		??/mingw-w64-gcc \
		??/mingw-w64-headers \
		??/mingw-w64-winpthreads \
		??/osslsigncode \
		??/upx \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
