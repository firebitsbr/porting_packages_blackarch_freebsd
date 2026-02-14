PORTNAME=	xplico
DISTVERSION=	1.2.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Internet Traffic Decoder. Network Forensic Analysis Tool (NFAT).
WWW=		https://github.com/xplico/xplico/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/dpkg \
		devel/git

RUN_DEPENDS=	??/apache \
		??/geoip \
		??/json-c \
		??/lame \
		??/libmariadbclient \
		??/libmaxminddb \
		??/libnet \
		??/libpqxx \
		??/ndpi \
		??/net-tools \
		??/perl \
		??/php-apache \
		??/php-pear \
		??/php-sqlite \
		??/py-httplib2@${PY_FLAVOR} \
		??/py-psycopg2@${PY_FLAVOR} \
		??/recode \
		??/sox \
		??/sqlite3 \
		??/tcpdump \
		lang/php82 \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
