PORTNAME=	python-arsenic
DISTVERSION=	21.8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Async WebDriver implementation for asyncio and asyncio-compatible frameworks.
WWW=		https://github.com/HDE/arsenic/releases

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/geckodriver \
		??/py-aiohttp@${PY_FLAVOR} \
		??/py-attrs@${PY_FLAVOR} \
		??/py-build@${PY_FLAVOR} \
		??/py-structlog@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
