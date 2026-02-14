PORTNAME=	limelighter
DISTVERSION=	17.d119dc7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool for generating fake code signing certificates or signing real ones.
WWW=		https://github.com/Tylous/Limelighter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		lang/go

RUN_DEPENDS=	??/osslsigncode \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
