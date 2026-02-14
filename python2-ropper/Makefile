PORTNAME=	python2-ropper
DISTVERSION=	1.13.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Display information about files in different file formats and find gadgets to build rop chains for different architectures (x86/x86_64, ARM/ARM64, MIPS, PowerPC, SPARC64).
WWW=		https://github.com/sashs/Ropper

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-capstone@${PY_FLAVOR} \
		??/py-filebytes@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-capstone@${PY_FLAVOR} \
		??/py-filebytes@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
