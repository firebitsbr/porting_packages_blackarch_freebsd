PORTNAME=	python2-cliff
DISTVERSION=	2.18.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Command Line Interface Formulation Framework.
WWW=		https://pypi.org/project/cliff/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cmd2@${PY_FLAVOR} \
		??/py-pbr@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		??/py-stevedore@${PY_FLAVOR} \
		??/py-unicodecsv@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
