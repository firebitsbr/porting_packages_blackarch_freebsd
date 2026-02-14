PORTNAME=	python-zeo
DISTVERSION=	6.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A client-server storage for ZODB for sharing a single storage among many clients.
WWW=		https://pypi.org/project/ZEO/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-persistent@${PY_FLAVOR} \
		??/py-transaction@${PY_FLAVOR} \
		??/py-zc.lockfile@${PY_FLAVOR} \
		??/py-zconfig@${PY_FLAVOR} \
		??/py-zdaemon@${PY_FLAVOR} \
		??/py-zodb@${PY_FLAVOR} \
		??/py-zope-interface@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
