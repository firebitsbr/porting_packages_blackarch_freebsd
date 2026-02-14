PORTNAME=	python-aiosmb
DISTVERSION=	0.4.14
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Fully asynchronous SMB library written in pure python.
WWW=		https://pypi.org/project/aiosmb/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiocmd@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-minikerberos@${PY_FLAVOR} \
		??/py-winsspi@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
