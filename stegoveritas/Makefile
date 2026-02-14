PORTNAME=	stegoveritas
DISTVERSION=	1.10
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automatic image steganography analysis tool.
WWW=		https://github.com/bannsec/stegoVeritas/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/binwalk \
		??/exempi \
		??/foremost \
		??/p7zip \
		??/perl-image-exiftool \
		??/py-apng@${PY_FLAVOR} \
		??/py-distro@${PY_FLAVOR} \
		??/py-exifread@${PY_FLAVOR} \
		??/py-magic@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-pyexiftool@${PY_FLAVOR} \
		??/py-pypng@${PY_FLAVOR} \
		??/py-stegoveritas-pfp@${PY_FLAVOR} \
		??/py-xmp-toolkit@${PY_FLAVOR} \
		??/steghide \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
