PORTNAME=	one-lin3r
DISTVERSION=	66.711a040
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Gives you one-liners that aids in penetration testing and more.
WWW=		https://github.com/D4Vinci/One-Lin3r

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-pyperclip@${PY_FLAVOR} \
		??/py-terminaltables@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
