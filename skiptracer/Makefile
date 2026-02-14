PORTNAME=	skiptracer
DISTVERSION=	123.ca40957
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OSINT python2 webscraping framework. Skipping the needs of API keys.
WWW=		https://github.com/84KaliPleXon3/skiptracer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-cfscrape@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-docx@${PY_FLAVOR} \
		??/py-ipdb@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
