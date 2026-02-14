PORTNAME=	vlan-hopping
DISTVERSION=	21.a37ba4e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Easy 802.1Q VLAN Hopping
WWW=		https://github.com/nccgroup/vlan-hopping

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/arp-scan \
		??/dmidecode \
		??/ethtool \
		??/metasploit \
		??/screen \
		??/vlan \
		??/wireshark-cli \
		??/yersinia \
		shells/bash


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
