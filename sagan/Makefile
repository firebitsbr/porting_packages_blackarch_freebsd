PORTNAME=	sagan
DISTVERSION=	2.0.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A snort-like log analysis engine.
WWW=		https://quadrantsec.com/sagan_log_analysis_engine/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/geoip \
		??/geoip-database \
		??/geoip-database-extra \
		??/geoip2-database \
		??/json-c \
		??/libesmtp \
		??/libfastjson \
		??/liblognorm \
		??/libyaml \
		??/mariadb-clients \
		??/pcre \
		??/postgresql-libs \
		??/sagan-rules \
		net/libdnet


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
