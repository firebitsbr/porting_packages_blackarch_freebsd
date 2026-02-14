PORTNAME=	regipy
DISTVERSION=	2.2.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Library for parsing offline registry hives.
WWW=		https://github.com/mkorman90/regipy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-attrs@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-construct@${PY_FLAVOR} \
		??/py-inflection@${PY_FLAVOR} \
		??/py-jsonlines@${PY_FLAVOR} \
		??/py-logbook@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
