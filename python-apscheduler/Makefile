PORTNAME=	python-apscheduler
DISTVERSION=	3.11.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	In-process task scheduler with Cron-like capabilities,
WWW=		https://github.com/agronholm/apscheduler

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-pytz@${PY_FLAVOR} \
		??/py-tzlocal@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
