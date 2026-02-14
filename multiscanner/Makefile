PORTNAME=	multiscanner
DISTVERSION=	1559.86e0145
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Modular file scanning/analysis framework.
WWW=		https://github.com/mitre/multiscanner

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-bitstring@${PY_FLAVOR} \
		??/py-configparser@${PY_FLAVOR} \
		??/py-elasticsearch@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-magic@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-pyclamd@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		??/py-sqlalchemy-utils@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/py-ssdeep@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
