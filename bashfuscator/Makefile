PORTNAME=	bashfuscator
DISTVERSION=	338.7487348
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Fully configurable and extendable Bash obfuscation framework.
WWW=		https://github.com/Bashfuscator/Bashfuscator

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-argcomplete@${PY_FLAVOR} \
		??/py-pyperclip@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
