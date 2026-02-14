PORTNAME=	vivisect
DISTVERSION=	v1.3.0.r0.g9c1573e8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python based static analysis and reverse engineering framework.
WWW=		https://github.com/vivisect/vivisect

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cxxfilt@${PY_FLAVOR} \
		??/py-msgpack@${PY_FLAVOR} \
		??/py-pyasn1-modules@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pycparser@${PY_FLAVOR} \
		??/py-pyqt5-webengine@${PY_FLAVOR} \
		??/py-pyqt5@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
