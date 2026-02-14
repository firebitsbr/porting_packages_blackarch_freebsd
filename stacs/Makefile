PORTNAME=	stacs
DISTVERSION=	0.5.1.r0.g11f3503
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Static Token And Credential Scanner.
WWW=		https://github.com/stacscan/stacs

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-click@${PY_FLAVOR} \
		??/py-libarchive@${PY_FLAVOR} \
		??/py-pydantic@${PY_FLAVOR} \
		??/py-yara-dex@${PY_FLAVOR} \
		??/pybind11 \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
