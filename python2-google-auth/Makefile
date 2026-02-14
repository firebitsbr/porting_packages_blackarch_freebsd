PORTNAME=	python2-google-auth
DISTVERSION=	1.7.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Google Authentication Library
WWW=		https://pypi.org/project/google-auth/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/ca-certificates \
		??/py-cachetools@${PY_FLAVOR} \
		??/py-pyasn1-modules@${PY_FLAVOR} \
		??/py-rsa@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
