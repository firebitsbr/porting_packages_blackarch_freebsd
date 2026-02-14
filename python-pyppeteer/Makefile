PORTNAME=	python-pyppeteer
DISTVERSION=	2.0.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Headless chrome/chromium automation library.
WWW=		https://github.com/pyppeteer/pyppeteer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-poetry-core@${PY_FLAVOR}

RUN_DEPENDS=	??/py-appdirs@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-pyee@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-websockets@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
