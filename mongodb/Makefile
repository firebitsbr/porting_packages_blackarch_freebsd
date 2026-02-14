PORTNAME=	mongodb
DISTVERSION=	8.2.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A high-performance, open source, schema-free document-oriented database.
WWW=		https://www.mongodb.com/try/download/community

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/chrpath

RUN_DEPENDS=	??/mongosh \
		ftp/curl \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
