PORTNAME=	sslyze
DISTVERSION=	6.3.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python tool for analyzing the configuration of SSL servers and for identifying misconfigurations.
WWW=		https://github.com/nabla-c0d3/sslyze

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cryptography@${PY_FLAVOR} \
		??/py-nassl@${PY_FLAVOR} \
		??/py-pydantic@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-tls-parser@${PY_FLAVOR} \
		??/py-typing_extensions@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
