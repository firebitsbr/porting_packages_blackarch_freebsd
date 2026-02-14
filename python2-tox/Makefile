PORTNAME=	python2-tox
DISTVERSION=	3.24.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A generic virtualenv management and test command line tool.
WWW=		https://tox.readthedocs.io/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-filelock@${PY_FLAVOR} \
		??/py-freezegun@${PY_FLAVOR} \
		??/py-pluggy@${PY_FLAVOR} \
		??/py-py@${PY_FLAVOR} \
		??/py-setuptools-scm@${PY_FLAVOR} \
		??/py-toml@${PY_FLAVOR} \
		??/py-virtualenv@${PY_FLAVOR}

RUN_DEPENDS=	??/py-filelock@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-pluggy@${PY_FLAVOR} \
		??/py-py@${PY_FLAVOR} \
		??/py-toml@${PY_FLAVOR} \
		??/py-virtualenv@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
