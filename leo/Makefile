PORTNAME=	leo
DISTVERSION=	37245.2be2ea110
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Literate programmers editor, outliner, and project manager.
WWW=		https://github.com/leo-editor/leo-editor/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	archivers/unzip \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-flask@${PY_FLAVOR} \
		??/py-pmw@${PY_FLAVOR} \
		??/py-pyqt5@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		??/tk \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
