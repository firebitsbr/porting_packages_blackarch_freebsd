PORTNAME=	python-pyattck
DISTVERSION=	7.1.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python Module to interact with the Mitre ATT&CK Framework.
WWW=		https://pypi.org/project/pyattck/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-fire@${PY_FLAVOR} \
		??/py-pendulum@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pyaml@${PY_FLAVOR} \
		??/py-pyfiglet@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
