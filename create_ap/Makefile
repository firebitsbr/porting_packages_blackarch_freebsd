PORTNAME=	create_ap
DISTVERSION=	265.462c09f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A shell script to create a NATed/Bridged Software Access Point.
WWW=		https://github.com/oblique/create_ap

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/dnsmasq \
		??/hostapd \
		??/iproute2 \
		??/iptables \
		??/iw \
		??/procps-ng \
		??/util-linux \
		??/which \
		shells/bash


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
