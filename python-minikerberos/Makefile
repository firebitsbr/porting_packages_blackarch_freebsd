PORTNAME=	python-minikerberos
DISTVERSION=	0.4.9
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Kerberos manipulation library in pure Python.
WWW=		https://pypi.org/project/minikerberos/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-asn1crypto@${PY_FLAVOR} \
		??/py-asysocks@${PY_FLAVOR} \
		??/py-oscrypto@${PY_FLAVOR} \
		??/py-unicrypto@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
