PORTNAME=	python2-pgcli
DISTVERSION=	4.1.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	CLI for Postgres Database. With auto-completion and syntax highlighting.
WWW=		https://pypi.org/project/pgcli/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cli-helpers@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-configobj@${PY_FLAVOR} \
		??/py-humanize@${PY_FLAVOR} \
		??/py-pgspecial@${PY_FLAVOR} \
		??/py-psycopg2@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-setproctitle@${PY_FLAVOR} \
		??/py-sqlparse@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
