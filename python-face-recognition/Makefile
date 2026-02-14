PORTNAME=	python-face-recognition
DISTVERSION=	1.3.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The worlds simplest facial recognition api for Python and the command line.
WWW=		https://pypi.org/project/face_recognition/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-click@${PY_FLAVOR} \
		??/py-dlib@${PY_FLAVOR} \
		??/py-face-recognition-models@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-scipy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
