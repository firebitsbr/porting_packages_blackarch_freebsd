PORTNAME=	python-witnessme
DISTVERSION=	1.5.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Web Inventory tool, takes screenshots of webpages using Pyppeteer.
WWW=		https://pypi.org/project/witnessme/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiodns@${PY_FLAVOR} \
		??/py-aiosqlite@${PY_FLAVOR} \
		??/py-appdirs@${PY_FLAVOR} \
		??/py-imgcat@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-pyee@${PY_FLAVOR} \
		??/py-pyppeteer@${PY_FLAVOR} \
		??/py-terminaltables@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-wcwidth@${PY_FLAVOR} \
		??/py-websockets@${PY_FLAVOR} \
		??/py-xmltodict@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
