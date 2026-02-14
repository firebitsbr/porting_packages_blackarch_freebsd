PORTNAME=	python2-flake8
DISTVERSION=	3.8.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The modular source code checker: pep8, pyflakes and co.
WWW=		https://pypi.org/project/flake8/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-configparser@${PY_FLAVOR} \
		??/py-entrypoints@${PY_FLAVOR} \
		??/py-enum34@${PY_FLAVOR} \
		??/py-functools32@${PY_FLAVOR} \
		??/py-mccabe@${PY_FLAVOR} \
		??/py-pycodestyle@${PY_FLAVOR} \
		??/py-pyflakes@${PY_FLAVOR} \
		??/py-typing@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
