PORTNAME=	torctl
DISTVERSION=	0.5.7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Script to redirect all traffic through tor network including dns queries for anonymizing entire system.
WWW=		https://github.com/BlackArch/torctl

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/iproute2 \
		??/iptables \
		??/macchanger \
		??/secure-delete \
		??/systemd \
		??/tor \
		ftp/curl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
