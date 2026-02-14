PORTNAME=	python2-celery
DISTVERSION=	4.3.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Distributed Asynchronous Task Queue.
WWW=		http://celeryproject.org/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-billiard@${PY_FLAVOR} \
		??/py-kombu@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
