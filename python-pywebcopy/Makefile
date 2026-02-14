PORTNAME=	python-pywebcopy
DISTVERSION=	7.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python package for cloning complete webpages and websites to local storage.
WWW=		https://pypi.org/project/pywebcopy/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cachecontrol@${PY_FLAVOR} \
		??/py-lxml-html-clean@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
