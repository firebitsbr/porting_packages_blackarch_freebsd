PORTNAME=	python2-paramiko
DISTVERSION=	2.12.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	SSH2 protocol library.
WWW=		https://pypi.org/project/paramiko/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-bcrypt@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pynacl@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
