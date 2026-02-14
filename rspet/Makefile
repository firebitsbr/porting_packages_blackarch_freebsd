PORTNAME=	rspet
DISTVERSION=	263.de4356e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python based reverse shell equipped with functionalities that assist in a post exploitation scenario.
WWW=		https://github.com/panagiks/RSPET

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-pip@${PY_FLAVOR} \
		devel/git

RUN_DEPENDS=	??/py-flask-cors@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
