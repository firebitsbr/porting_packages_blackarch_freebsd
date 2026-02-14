PORTNAME=	python-apksigtool
DISTVERSION=	0.1.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Parse & verify android apk signing blocks.
WWW=		https://pypi.org/project/apksigtool/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/apksigcopier \
		??/py-asn1crypto@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
