PORTNAME=	darkscrape
DISTVERSION=	68.2ca0e37
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OSINT Tool For Scraping Dark Websites.
WWW=		https://github.com/itsmehacker/DarkScrape

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-face-recognition@${PY_FLAVOR} \
		??/py-xlrd@${PY_FLAVOR} \
		??/tor \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
