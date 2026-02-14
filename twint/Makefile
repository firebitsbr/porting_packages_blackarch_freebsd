PORTNAME=	twint
DISTVERSION=	845.e7c8a0c7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An advanced Twitter scraping & OSINT tool written in Python that doesnt use Twitters API, allowing you to scrape a users followers, following, Tweets and more while evading most API limitations.
WWW=		https://github.com/twintproject/twint

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiodns@${PY_FLAVOR} \
		??/py-aiohttp-socks@${PY_FLAVOR} \
		??/py-aiohttp@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-cchardet@${PY_FLAVOR} \
		??/py-elasticsearch@${PY_FLAVOR} \
		??/py-fake-useragent@${PY_FLAVOR} \
		??/py-geopy@${PY_FLAVOR} \
		??/py-googletransx@${PY_FLAVOR} \
		??/py-pandas@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-schedule@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
