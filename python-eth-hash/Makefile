PORTNAME=	python-eth-hash
DISTVERSION=	0.7.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The Ethereum hashing function, keccak256, sometimes (erroneously) called sha3.
WWW=		https://pypi.org/project/eth-hash/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
