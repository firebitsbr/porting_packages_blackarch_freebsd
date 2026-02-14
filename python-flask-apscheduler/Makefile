PORTNAME=	python-flask-apscheduler
DISTVERSION=	1.13.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Adds APScheduler support to Flask.
WWW=		https://pypi.org/project/Flask-apscheduler/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-apscheduler@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
