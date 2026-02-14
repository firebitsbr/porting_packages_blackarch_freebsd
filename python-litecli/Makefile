PORTNAME=	python-litecli
DISTVERSION=	1.17.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	CLI for SQLite Databases with auto-completion and syntax highlighting.
WWW=		https://pypi.org/project/litecli/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cli-helpers@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-configobj@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-sqlparse@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
