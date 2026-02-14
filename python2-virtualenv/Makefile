PORTNAME=	python2-virtualenv
DISTVERSION=	20.13.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Virtual Python Environment builder.
WWW=		https://pypi.org/project/virtualenv/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-pip@${PY_FLAVOR} \
		??/py-setuptools-scm@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-backports.entry-points-selectable@${PY_FLAVOR} \
		??/py-distlib@${PY_FLAVOR} \
		??/py-filelock@${PY_FLAVOR} \
		??/py-importlib-metadata@${PY_FLAVOR} \
		??/py-importlib_resources@${PY_FLAVOR} \
		??/py-pathlib2@${PY_FLAVOR} \
		??/py-platformdirs@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
