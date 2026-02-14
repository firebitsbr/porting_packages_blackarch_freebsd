PORTNAME=	procdump
DISTVERSION=	3.5.0.r1.g7a0392b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Generate coredumps based off performance triggers.
WWW=		https://github.com/Microsoft/ProcDump-for-Linux

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/bpf \
		??/clang \
		??/cmake \
		??/libbpf \
		devel/git

RUN_DEPENDS=	??/gdb


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
