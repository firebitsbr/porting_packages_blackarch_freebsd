PORTNAME=	villain
DISTVERSION=	V2.2.1.r3.g87e5dd1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	C2 framework that can handle multiple TCP socket & HoaxShell-based reverse shells, enhance their functionality with additional features and share them among connected sibling servers.
WWW=		https://github.com/t3l3machus/Villain

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-gnureadline@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pycryptodomex@${PY_FLAVOR} \
		??/py-pyperclip@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
