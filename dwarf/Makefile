PORTNAME=	dwarf
DISTVERSION=	1084.fd859ae
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Full featured multi arch/os debugger built on top of PyQt5 and frida.
WWW=		https://github.com/iGio90/Dwarf

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-capstone@${PY_FLAVOR} \
		??/py-event-bus@${PY_FLAVOR} \
		??/py-frida@${PY_FLAVOR} \
		??/py-hexdump@${PY_FLAVOR} \
		??/py-pyperclip@${PY_FLAVOR} \
		??/py-pyqt5@${PY_FLAVOR} \
		??/py-qdarkstyle@${PY_FLAVOR} \
		??/py-unicorn@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
