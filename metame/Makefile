PORTNAME=	metame
DISTVERSION=	14.8d583a0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A simple metamorphic code engine for arbitrary executables.
WWW=		https://github.com/a0rtega/metame

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-keystone@${PY_FLAVOR} \
		??/py-r2pipe@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/radare2 \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
