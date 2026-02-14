PORTNAME=	pocsuite
DISTVERSION=	430.877d1b1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An open-sourced remote vulnerability testing framework developed by the Knownsec Security Team.
WWW=		https://github.com/knownsec/Pocsuite

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-lxml@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
