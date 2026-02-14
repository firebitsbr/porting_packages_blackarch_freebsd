PORTNAME=	isme
DISTVERSION=	0.12
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Scans a VOIP environment, adapts to enterprise VOIP, and exploits the possibilities of being connected directly to an IP Phone VLAN.
WWW=		https://packetstormsecurity.com/files/123534/IP-Phone-Scanning-Made-Easy-0.12.html

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	archivers/unzip

RUN_DEPENDS=	??/perl \
		??/perl-crypt-ssleay \
		??/perl-html-parser \
		??/perl-http-date \
		??/perl-http-message \
		??/perl-libwww \
		??/perl-lwp-protocol-https \
		??/perl-mozilla-ca \
		??/perl-net-dhcp \
		??/perl-net-libdnet \
		??/perl-net-netmask \
		??/perl-net-ping \
		??/perl-net-rawip \
		??/perl-net-ssh-perl \
		??/perl-net-subnet \
		??/perl-net-tftp \
		??/perl-tk


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
