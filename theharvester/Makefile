PORTNAME=	theharvester
DISTVERSION=	4.10.0.r12.g419291a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	E-mails, subdomains and names Harvester - OSINT
WWW=		https://github.com/laramies/theHarvester

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/flake8 \
		??/py-aiodns@${PY_FLAVOR} \
		??/py-aiofiles@${PY_FLAVOR} \
		??/py-aiohttp-socks@${PY_FLAVOR} \
		??/py-aiohttp@${PY_FLAVOR} \
		??/py-aiomultiprocess@${PY_FLAVOR} \
		??/py-aiosqlite@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-censys@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-fastapi@${PY_FLAVOR} \
		??/py-gevent@${PY_FLAVOR} \
		??/py-grequests@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-mypy_extensions@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-orjson@${PY_FLAVOR} \
		??/py-playwright@${PY_FLAVOR} \
		??/py-plotly@${PY_FLAVOR} \
		??/py-pyppeteer@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		??/py-retrying@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-slowapi@${PY_FLAVOR} \
		??/py-starlette@${PY_FLAVOR} \
		??/py-texttable@${PY_FLAVOR} \
		??/py-typing_extensions@${PY_FLAVOR} \
		??/py-ujson@${PY_FLAVOR} \
		??/py-uvloop@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		??/py-zope-event@${PY_FLAVOR} \
		??/uvicorn \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
