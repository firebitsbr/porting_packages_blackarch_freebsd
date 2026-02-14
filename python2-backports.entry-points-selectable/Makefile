PORTNAME=	python2-backports.entry-points-selectable
DISTVERSION=	66.d4b54f4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Compatibility shim providing selectable entry points for older implementations.
WWW=		https://github.com/jaraco/backports.entry_points_selectable

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-backports@${PY_FLAVOR} \
		??/py-funcsigs@${PY_FLAVOR} \
		??/py-pluggy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
