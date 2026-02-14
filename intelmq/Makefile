PORTNAME=	intelmq
DISTVERSION=	3.5.0.r5.g5b76b3645
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool for collecting and processing security feeds using a message queuing protocol.
WWW=		https://github.com/certtools/intelmq

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dateutil@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-psycopg2@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-redis@${PY_FLAVOR} \
		??/py-ruamel-yaml@${PY_FLAVOR} \
		??/py-termstyle@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
