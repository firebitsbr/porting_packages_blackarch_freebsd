PORTNAME=	gloom
DISTVERSION=	93.cd6e927
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Linux Penetration Testing Framework.
WWW=		https://github.com/StreetSec/Gloom-Framework

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-geoip@${PY_FLAVOR} \
		??/py-mechanize@${PY_FLAVOR} \
		??/py-pythonwhois@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/wifijammer \
		ftp/curl \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR} \
		security/nmap \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
