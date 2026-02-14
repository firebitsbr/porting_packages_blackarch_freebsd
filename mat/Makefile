PORTNAME=	mat
DISTVERSION=	0.6.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Metadata Anonymisation Toolkit composed of a GUI application, a CLI application and a library.
WWW=		https://mat.boum.org/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/hachoir-core \
		??/hachoir-parser \
		??/py-cairo@${PY_FLAVOR} \
		??/py-distutils-extra@${PY_FLAVOR} \
		??/py-mutagen@${PY_FLAVOR} \
		??/py-pdfrw@${PY_FLAVOR} \
		??/py-poppler@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
