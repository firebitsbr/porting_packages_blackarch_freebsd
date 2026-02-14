PORTNAME=	pg-gvm
DISTVERSION=	22.6.9
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Greenbone Library for helper functions in PostgreSQL.
WWW=		https://github.com/greenbone/pg-gvm

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/doxygen \
		??/xmltoman \
		textproc/libxslt

RUN_DEPENDS=	??/glib2 \
		??/gvm-libs \
		??/libical \
		??/postgresql


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
