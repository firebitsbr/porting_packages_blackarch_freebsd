PORTNAME=	frida-disasm
DISTVERSION=	284.79d63f5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An interactive disassembler based on LLVM and Qt.
WWW=		https://www.frida.xyz/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/pkg-config \
		devel/git

RUN_DEPENDS=	??/boost \
		??/gmock \
		??/guile \
		??/libedit \
		??/llvm35 \
		??/log4cxx \
		??/quazip \
		??/swig


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
