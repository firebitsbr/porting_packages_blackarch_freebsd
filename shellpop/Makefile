PORTNAME=	shellpop
DISTVERSION=	148.a145349
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Generate easy and sophisticated reverse or bind shell commands.
WWW=		https://github.com/0x00-0x00/ShellPop

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-argcomplete@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-pyperclip@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
