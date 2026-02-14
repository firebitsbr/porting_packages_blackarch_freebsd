PORTNAME=	enteletaor
DISTVERSION=	68.a975b5c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Message Queue & Broker Injection tool that implements attacks to Redis, RabbitMQ and ZeroMQ.
WWW=		https://github.com/cr0hn/enteletaor

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-amqp@${PY_FLAVOR} \
		??/py-celery@${PY_FLAVOR} \
		??/py-colorlog@${PY_FLAVOR} \
		??/py-eventlet@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-kombu@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-markupsafe@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-pyzmq@${PY_FLAVOR} \
		??/py-redis@${PY_FLAVOR} \
		??/py-wtforms@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
