PORTNAME=	driftnet
DISTVERSION=	v1.6.0.r0.g4c8a849
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Listens to network traffic and picks out images from TCP streams it observes.
WWW=		http://www.ex-parrot.com/~chris/driftnet/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/imake \
		devel/git

RUN_DEPENDS=	??/giflib \
		??/gtk2 \
		??/libjpeg \
		??/libwebsockets \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
