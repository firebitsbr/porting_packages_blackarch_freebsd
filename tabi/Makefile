PORTNAME=	tabi
DISTVERSION=	13.068a406
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	BGP Hijack Detection.
WWW=		https://github.com/ANSSI-FR/tabi

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dateutil@${PY_FLAVOR} \
		??/py-radix@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
