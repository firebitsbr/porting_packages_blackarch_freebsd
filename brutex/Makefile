PORTNAME=	brutex
DISTVERSION=	114.eacd084
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automatically brute force all services running on a target.
WWW=		https://github.com/1N3/BruteX

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/dnsenum \
		??/hydra \
		??/masscan \
		??/net-snmp \
		security/nmap \
		shells/bash


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
