PORTNAME=	cottontail
DISTVERSION=	93.b7f5222
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Capture all RabbitMQ messages being sent through a broker.
WWW=		https://github.com/QKaiser/cottontail

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-coloredlogs@${PY_FLAVOR} \
		??/py-pika@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-verboselogs@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
