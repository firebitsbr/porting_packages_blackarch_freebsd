PORTNAME=	python2-flask-openid
DISTVERSION=	1.2.5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OpenID support for Flask.
WWW=		https://pypi.org/project/flask-openid/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-flask@${PY_FLAVOR} \
		??/py-openid@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
