PORTNAME=	dnsenum
DISTVERSION=	1.2.4.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Script that enumerates DNS information from a domain, attempts zone transfers, performs a brute force dictionary style attack, and then performs reverse look-ups on the results.
WWW=		https://github.com/fwaeytens/dnsenum/

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/perl \
		??/perl-net-dns \
		??/perl-net-ip \
		??/perl-net-netmask \
		??/perl-net-whois-ip \
		??/perl-string-random \
		??/perl-www-mechanize \
		??/perl-xml-writer


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
