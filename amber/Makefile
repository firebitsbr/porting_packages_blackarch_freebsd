PORTNAME=	amber
DISTVERSION=	v3.1.r2.gf6eb2dc
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Reflective PE packer.
WWW=		https://github.com/EgeBalci/Amber

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		lang/go

RUN_DEPENDS=	??/gcc-multilib \
		??/keystone \
		??/mingw-w64-binutils \
		??/mingw-w64-crt \
		??/mingw-w64-gcc \
		??/mingw-w64-headers \
		??/mingw-w64-headers-bootstrap \
		??/mingw-w64-winpthreads \
		??/nasm


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
