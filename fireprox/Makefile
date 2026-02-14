PORTNAME=	fireprox
DISTVERSION=	51.a6e1300
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	AWS API Gateway management tool for creating on the fly HTTP pass-through proxies for unique IP rotation.
WWW=		https://github.com/ustayready/fireprox

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-virtualenv@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
