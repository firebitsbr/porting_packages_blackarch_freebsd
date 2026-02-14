PORTNAME=	python-censys
DISTVERSION=	2.2.19
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python library for interacting with Censys Search Engine (censys.io).
WWW=		https://pypi.org/project/censys/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-poetry@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-argcomplete@${PY_FLAVOR} \
		??/py-backoff@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
