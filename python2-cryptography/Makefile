PORTNAME=	python2-cryptography
DISTVERSION=	3.3.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A package which provides cryptographic recipes and primitives to Python developers.
WWW=		https://pypi.org/project/cryptography/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-asn1crypto@${PY_FLAVOR} \
		??/py-cffi@${PY_FLAVOR} \
		??/py-enum34@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-ipaddress@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
