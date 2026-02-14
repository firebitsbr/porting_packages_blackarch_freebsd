PORTNAME=	sandy
DISTVERSION=	6.531ab16
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An open-source Samsung phone encryption assessment framework
WWW=		https://github.com/donctl/sandy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pbkdf2@${PY_FLAVOR} \
		??/py-pexpect@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
