PORTNAME=	sslsniff
DISTVERSION=	0.8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool to MITM all SSL connections on a LAN and dynamically generate certs for the domains that are being accessed on the fly.
WWW=		https://github.com/moxie0/sslsniff

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/boost \
		??/dsniff \
		??/log4cpp


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
