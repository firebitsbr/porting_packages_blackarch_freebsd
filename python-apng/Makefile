PORTNAME=	python-apng
DISTVERSION=	0.3.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python module to deal with APNG files.
WWW=		https://github.com/eight04/pyAPNG

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-docutils@${PY_FLAVOR} \
		??/py-pathlib2@${PY_FLAVOR} \
		??/py-pylint@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		??/py-pyxcute@${PY_FLAVOR} \
		??/py-sphinx-autobuild@${PY_FLAVOR} \
		??/py-sphinx@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		??/twine


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
