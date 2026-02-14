PORTNAME=	torcrawl
DISTVERSION=	v1.35.r0.g0d6a29b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Crawl and extract (regular or onion) webpages through TOR network.
WWW=		https://github.com/MikeMeliz/TorCrawl.py

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-socks@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-yara-dex@${PY_FLAVOR} \
		??/tor \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
