PORTNAME=	uefi-firmware-parser
DISTVERSION=	193.0c5fb74
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Parse BIOS/Intel ME/UEFI firmware related structures: Volumes, FileSystems, Files, etc.
WWW=		https://github.com/theopolis/uefi-firmware-parser

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-pefile@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
