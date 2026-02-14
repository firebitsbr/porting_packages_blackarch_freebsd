PORTNAME=	praeda
DISTVERSION=	49.b0b17d3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An automated data/information harvesting tool designed to gather critical information from various embedded devices.
WWW=		https://github.com/percx/Praeda

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/perl \
		??/perl-crypt-ssleay \
		??/perl-html-tableextract \
		??/perl-html-tagparser \
		??/perl-http-cookies \
		??/perl-io-socket \
		??/perl-net-snmp \
		??/perl-net-ssleay \
		??/perl-netaddr-ip \
		??/perl-uri-fetch


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
