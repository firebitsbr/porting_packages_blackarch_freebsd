PORTNAME=	berate_ap
DISTVERSION=	v0.4.6.r98.g4ac163f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Script for orchestrating mana rogue WiFi Access Points.
WWW=		https://github.com/sensepost/berate_ap

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/dnsmasq \
		??/hostapd \
		??/iproute2 \
		??/iptables \
		??/iw \
		??/procps-ng \
		??/util-linux \
		shells/bash


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
