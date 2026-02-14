PORTNAME=	python2-parsel
DISTVERSION=	1.5.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A library to extract data from HTML and XML using XPath and CSS selectors.
WWW=		https://github.com/scrapy/parsel

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cssselect@${PY_FLAVOR} \
		??/py-functools32@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-w3lib@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
