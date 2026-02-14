PORTNAME=	python2-pygithub
DISTVERSION=	1.44.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Use the full Github API v3.
WWW=		https://github.com/PyGithub/PyGithub

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-deprecated@${PY_FLAVOR} \
		??/py-pyjwt@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
