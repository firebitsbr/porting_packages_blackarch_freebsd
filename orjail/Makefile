PORTNAME=	orjail
DISTVERSION=	200.ae38ba2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A more secure way to force programs to exclusively use tor network.
WWW=		https://github.com/orjail/orjail

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/bc \
		??/firejail \
		??/iptables \
		??/tor \
		shells/bash


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
