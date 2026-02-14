PORTNAME=	pmcma
DISTVERSION=	1.00
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automated exploitation of invalid memory writes (being them the consequences of an overflow in a writable section, of a missing format string, integer overflow, variable misuse, or any other type of memory corruption).
WWW=		http://packetstormsecurity.com/files/104724/Post-Memory-Corruption-Memory-Analyzer-1.00.html

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/bison \
		??/cmake \
		??/flex \
		??/gcc

RUN_DEPENDS=	??/bison \
		??/flex


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
