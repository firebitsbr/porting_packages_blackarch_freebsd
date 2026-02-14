PORTNAME=	python2-sphinx
DISTVERSION=	1.8.5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python documentation generator.
WWW=		https://pypi.org/project/sphinx/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-babel@${PY_FLAVOR} \
		??/py-docutils@${PY_FLAVOR} \
		??/py-imagesize@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-snowballstemmer@${PY_FLAVOR} \
		??/py-sphinx-alabaster-theme@${PY_FLAVOR} \
		??/py-sphinxcontrib-websupport@${PY_FLAVOR} \
		??/py-typing@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
