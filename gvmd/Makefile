PORTNAME=	gvmd
DISTVERSION=	26.0.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Greenbone Vulnerability Manager - The database backend for the Greenbone Community Edition.
WWW=		https://github.com/greenbone/gvmd

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/doxygen \
		??/xmltoman \
		textproc/libxslt

RUN_DEPENDS=	??/cjson \
		??/gnutls \
		??/gvm-libs \
		??/libbsd \
		??/libical \
		??/ospd-openvas \
		??/pg-gvm \
		??/postgresql \
		lang/python \
		textproc/libxslt


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
