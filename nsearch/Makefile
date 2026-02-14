PORTNAME=	nsearch
DISTVERSION=	353.bd8205b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Minimal script to help find script into the nse database.
WWW=		https://github.com/JKO/nsearch

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-i18n@${PY_FLAVOR} \
		??/py-nmap@${PY_FLAVOR} \
		??/py-pysqlite@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
