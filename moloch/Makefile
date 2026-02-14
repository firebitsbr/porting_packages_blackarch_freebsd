PORTNAME=	moloch
DISTVERSION=	0.11.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An open source large scale IPv4 full PCAP capturing, indexing and database system.
WWW=		https://github.com/aol/moloch

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/glib2

RUN_DEPENDS=	??/elasticsearch \
		??/file \
		??/geoip \
		??/libnids \
		??/libpng \
		??/perl-json \
		??/perl-libwww \
		??/util-linux \
		ftp/curl \
		lang/python3 \
		www/node


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
