PORTNAME=	onionsearch
DISTVERSION=	44.fc9d62c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Script that scrapes urls on different .onion search engines.
WWW=		https://github.com/megadose/OnionSearch

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-html5lib@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
