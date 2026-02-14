PORTNAME=	dff
DISTVERSION=	1.4.0.r0.gd40d46b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Forensics Framework coming with command line and graphical interfaces.
WWW=		https://github.com/arxsys/dff

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/flex \
		??/libbde \
		??/libbfio \
		??/libewf \
		??/libpff \
		??/libvshadow \
		??/pkg-config \
		??/swig \
		??/tre \
		devel/git

RUN_DEPENDS=	??/ffmpeg \
		??/libbde \
		??/libbfio \
		??/libewf \
		??/libpff \
		??/libvshadow \
		??/poppler-qt4 \
		??/py-apsw@${PY_FLAVOR} \
		??/py-magic@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-poppler-qt4@${PY_FLAVOR} \
		??/py-pyqt4@${PY_FLAVOR} \
		??/qt4 \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
