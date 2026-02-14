PORTNAME=	python-aesedb
DISTVERSION=	0.1.8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Async parser for NTDS.dit database file for obtaining user secrets and JET databases.
WWW=		https://pypi.org/project/aesedb/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiowinreg@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-pycryptodomex@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-unicrypto@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
