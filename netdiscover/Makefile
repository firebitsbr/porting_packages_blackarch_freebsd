PORTNAME=	netdiscover
DISTVERSION=	257.42648f9
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An active/passive address reconnaissance tool, mainly developed for those wireless networks without dhcp server, when you are wardriving. It can be also used on hub/switched networks.
WWW=		http://nixgeneration.com/~jaime/netdiscover/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/dos2unix \
		??/gcc \
		??/make \
		devel/git

RUN_DEPENDS=	??/libnet \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
