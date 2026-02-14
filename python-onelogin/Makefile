PORTNAME=	python-onelogin
DISTVERSION=	3.2.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OneLogin API.
WWW=		https://pypi.org/project/onelogin/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-certifi@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-frozendict@${PY_FLAVOR} \
		??/py-typing_extensions@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
