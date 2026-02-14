PORTNAME=	python-pyradamsa
DISTVERSION=	v0.1.1.r1.g8d1fdb5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python bindings for radamsa fuzzing library..
WWW=		https://github.com/tsundokul/$_pkgname

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git

RUN_DEPENDS=	??/py-pytest@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
