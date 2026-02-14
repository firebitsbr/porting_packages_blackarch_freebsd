PORTNAME=	hostapd-wpe
DISTVERSION=	2.11
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Modified hostapd to facilitate AP impersonation attacks.
WWW=		https://w1.fi/hostapd/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/libnl \
		??/openssl-1.0 \
		??/sqlite


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
