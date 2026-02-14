PORTNAME=	python-asciistuff
DISTVERSION=	1.3.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Library for producing ASCII arts from a text or an image.
WWW=		https://pypi.org/project/asciistuff/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cowpy@${PY_FLAVOR} \
		??/py-pyfiglet@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-terminaltables@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
