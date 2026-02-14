PORTNAME=	python-terminaltables
DISTVERSION=	3.1.10
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Generate simple tables in terminals from a nested list of strings.
WWW=		https://github.com/matthewdeanmartin/terminaltables

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-httpx@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-pbs-installer@${PY_FLAVOR} \
		??/py-poetry@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		??/py-zstandard@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
