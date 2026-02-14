PORTNAME=	python2-google-auth-httplib2
DISTVERSION=	0.0.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Google Authentication Library: httplib2 transport
WWW=		https://pypi.org/project/google-auth-httplib2/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-google-auth@${PY_FLAVOR} \
		??/py-httplib2@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
