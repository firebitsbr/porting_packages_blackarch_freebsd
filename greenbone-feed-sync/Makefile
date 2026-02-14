PORTNAME=	greenbone-feed-sync
DISTVERSION=	25.1.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	New script for downloading the Greenbone Community Feed.
WWW=		https://github.com/greenbone/greenbone-feed-sync

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-poetry@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR}

RUN_DEPENDS=	??/py-rich@${PY_FLAVOR} \
		??/py-shtab@${PY_FLAVOR} \
		??/py-tomli@${PY_FLAVOR} \
		??/rsync


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
