PORTNAME=	ftpscout
DISTVERSION=	12.cf1dff1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Scans ftps for anonymous access.
WWW=		https://github.com/RubenRocha/ftpscout

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-pika@${PY_FLAVOR} \
		??/rabbitmq \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
