PORTNAME=	python2-ssdeep
DISTVERSION=	3.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python wrapper for ssdeep fuzzy hashing library.
WWW=		https://pypi.org/project/ssdeep/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-cffi@${PY_FLAVOR} \
		??/py-pip@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		??/ssdeep \
		devel/py-setuptools@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cffi@${PY_FLAVOR} \
		??/ssdeep \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
