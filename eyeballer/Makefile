PORTNAME=	eyeballer
DISTVERSION=	143.5299227
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Convolutional neural network for analyzing pentest screenshots.
WWW=		https://github.com/BishopFox/eyeballer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	archivers/unzip \
		devel/git \
		ftp/wget

RUN_DEPENDS=	??/py-augmentor@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-matplotlib@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pandas@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-progressbar@${PY_FLAVOR} \
		??/py-scikit-learn@${PY_FLAVOR} \
		??/py-tensorflow@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
