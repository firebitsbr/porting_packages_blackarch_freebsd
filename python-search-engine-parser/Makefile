PORTNAME=	python-search-engine-parser
DISTVERSION=	0.6.8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Scrapes search engine pages for query titles, descriptions and links.
WWW=		https://pypi.org/project/search-engine-parser/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiohttp@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-blessed@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
