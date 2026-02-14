PORTNAME=	mercury
DISTVERSION=	2.13.1.r1.g570fba4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Network metadata capture and analysis.
WWW=		https://github.com/cisco/mercury

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/clang \
		??/gcc \
		??/tcpreplay \
		??/valgrind \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/gmp \
		??/zlib \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
