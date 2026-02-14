PORTNAME=	backdoorme
DISTVERSION=	308.f9755ca
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A powerful utility capable of backdooring Unix machines with a slew of backdoors.
WWW=		https://github.com/Kkevsterrr/backdoorme

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-pexpect@${PY_FLAVOR} \
		??/py-rpyc@${PY_FLAVOR} \
		??/py-scp@${PY_FLAVOR} \
		??/tk \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
