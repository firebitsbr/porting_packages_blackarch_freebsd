PORTNAME=	python-asyauth
DISTVERSION=	0.0.23
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Unified authentication library.
WWW=		https://pypi.org/project/asyauth/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-asn1crypto@${PY_FLAVOR} \
		??/py-asysocks@${PY_FLAVOR} \
		??/py-minikerberos@${PY_FLAVOR} \
		??/py-unicrypto@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
