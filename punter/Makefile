PORTNAME=	punter
DISTVERSION=	45.97b7bed
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Hunt domain names using DNSDumpster, WHOIS, Reverse WHOIS, Shodan, Crimeflare.
WWW=		https://github.com/nethunteros/punter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-api-dnsdumpster@${PY_FLAVOR} \
		??/py-argparse@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-configparser@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-ipaddr@${PY_FLAVOR} \
		??/py-ipwhois@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
