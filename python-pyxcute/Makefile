PORTNAME=	python-pyxcute
DISTVERSION=	0.8.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A small task runner inspired by npm scripts.
WWW=		https://pypi.org/project/pyxcute/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-docutils@${PY_FLAVOR} \
		??/py-livereload@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pylint@${PY_FLAVOR} \
		??/py-sphinx-autobuild@${PY_FLAVOR} \
		??/py-sphinx@${PY_FLAVOR} \
		??/twine \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
