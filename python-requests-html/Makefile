PORTNAME=	python-requests-html
DISTVERSION=	462.075ac16
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Pythonic HTML Parsing for Humans.
WWW=		https://github.com/psf/requests-html

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-fake-useragent@${PY_FLAVOR} \
		??/py-parse@${PY_FLAVOR} \
		??/py-pyppeteer@${PY_FLAVOR} \
		??/py-pyquery@${PY_FLAVOR} \
		??/py-w3lib@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
