PORTNAME=	redis
DISTVERSION=	8.0.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An in-memory database that persists on disk.
WWW=		https://redis.io/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/systemd \
		security/openssl

RUN_DEPENDS=	??/grep \
		??/jemalloc \
		??/shadow \
		??/systemd-libs


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
