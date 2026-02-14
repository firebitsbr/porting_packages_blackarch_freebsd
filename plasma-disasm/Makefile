PORTNAME=	plasma-disasm
DISTVERSION=	922.ec7df9b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An interactive disassembler for x86/ARM/MIPS. It can generates indented pseudo-code with colored syntax.
WWW=		https://github.com/joelpx/plasma

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-nose@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-capstone@${PY_FLAVOR} \
		??/py-msgpack@${PY_FLAVOR} \
		??/py-nose@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-pyelftools@${PY_FLAVOR} \
		??/py-pyqt4@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
