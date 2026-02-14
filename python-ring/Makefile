PORTNAME=	python-ring
DISTVERSION=	0.10.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python library that shows a way to control cache in point of view of code - not about storages.
WWW=		https://pypi.org/project/ring/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-diskcache@${PY_FLAVOR} \
		??/py-inspect2@${PY_FLAVOR} \
		??/py-mock@${PY_FLAVOR} \
		??/py-pymemcache@${PY_FLAVOR} \
		??/py-wirerope@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
