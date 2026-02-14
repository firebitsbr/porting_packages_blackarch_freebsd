PORTNAME=	usbrip
DISTVERSION=	291.5093c84
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	USB device artifacts tracker.
WWW=		https://github.com/snovvcrash/usbrip

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-termcolor@${PY_FLAVOR} \
		??/py-terminaltables@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
