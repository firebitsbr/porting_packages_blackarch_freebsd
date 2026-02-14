PORTNAME=	pshitt
DISTVERSION=	23.dae7931
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A lightweight fake SSH server designed to collect authentication data
WWW=		https://github.com/regit/pshitt

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-daemon@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
