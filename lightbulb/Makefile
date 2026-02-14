PORTNAME=	lightbulb
DISTVERSION=	88.9e8d6f3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python framework for auditing web applications firewalls.
WWW=		https://github.com/lightbulb-framework/lightbulb-framework

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-backports.functools_lru_cache@${PY_FLAVOR} \
		??/py-cliff@${PY_FLAVOR} \
		??/py-contextlib2@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-sfalearn@${PY_FLAVOR} \
		??/py-symautomata@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
