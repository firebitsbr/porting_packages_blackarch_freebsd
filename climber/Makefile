PORTNAME=	climber
DISTVERSION=	30.5530a78
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Check UNIX/Linux systems for privilege escalation.
WWW=		https://github.com/raffaele-forte/climber

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-exscript@${PY_FLAVOR} \
		??/py-mako@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
