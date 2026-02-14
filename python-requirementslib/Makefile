PORTNAME=	python-requirementslib
DISTVERSION=	2.3.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool for converting between pip-style and pipfile requirements.
WWW=		https://github.com/sarugaku/requirementslib

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-invoke@${PY_FLAVOR} \
		??/py-parver@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git

RUN_DEPENDS=	??/py-attrs@${PY_FLAVOR} \
		??/py-cached-property@${PY_FLAVOR} \
		??/py-cerberus@${PY_FLAVOR} \
		??/py-distlib@${PY_FLAVOR} \
		??/py-pep517@${PY_FLAVOR} \
		??/py-platformdirs@${PY_FLAVOR} \
		??/py-plette@${PY_FLAVOR} \
		??/py-tomlkit@${PY_FLAVOR} \
		??/py-vistir@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
