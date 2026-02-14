PORTNAME=	python-pypykatz
DISTVERSION=	0.6.13
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python implementation of Mimikatz.
WWW=		https://github.com/skelsec/pypykatz

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aesedb@${PY_FLAVOR} \
		??/py-aiosmb@${PY_FLAVOR} \
		??/py-aiowinreg@${PY_FLAVOR} \
		??/py-asyauth@${PY_FLAVOR} \
		??/py-minidump@${PY_FLAVOR} \
		??/py-minikerberos@${PY_FLAVOR} \
		??/py-msldap@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-unicrypto@${PY_FLAVOR} \
		??/py-winacl@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
