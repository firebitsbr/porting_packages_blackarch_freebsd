PORTNAME=	python2-gitpython
DISTVERSION=	3.0.5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A python library used to interact with Git repositories.
WWW=		https://github.com/gitpython-developers/gitpython

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-gitdb@${PY_FLAVOR} \
		devel/git


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
