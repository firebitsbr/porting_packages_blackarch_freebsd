PORTNAME=	python2-ndg-httpsclient
DISTVERSION=	0.5.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL.
WWW=		https://pypi.org/project/ndg-httpsclient/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-pyasn1@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
