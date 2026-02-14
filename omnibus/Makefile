PORTNAME=	omnibus
DISTVERSION=	129.88dbf5d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OSINT tool for intelligence collection, research and artifact management.
WWW=		https://github.com/InQuest/omnibus

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/mongodb \
		??/py-backports.functools_lru_cache@${PY_FLAVOR} \
		??/py-beautifulsoup3@${PY_FLAVOR} \
		??/py-censys@${PY_FLAVOR} \
		??/py-cmd2@${PY_FLAVOR} \
		??/py-contextlib2@${PY_FLAVOR} \
		??/py-cymon@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-fuzzyfinder@${PY_FLAVOR} \
		??/py-ipwhois@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		??/py-redis@${PY_FLAVOR} \
		??/py-threatcrowd@${PY_FLAVOR} \
		??/redis \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
