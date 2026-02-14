PORTNAME=	klee
DISTVERSION=	2.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A symbolic virtual machine built on top of the LLVM compiler infrastructure.
WWW=		https://github.com/klee/klee

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/clang \
		??/cmake \
		??/gperftools \
		??/llvm \
		??/z3 \
		devel/git

RUN_DEPENDS=	??/gperftools \
		??/klee-uclibc \
		??/libcap \
		??/llvm-libs \
		??/sqlite \
		??/z3 \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
