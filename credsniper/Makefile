PORTNAME=	credsniper
DISTVERSION=	21.f52461b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Phishing framework written with the Python micro-framework Flask and Jinja2 templating which supports capturing 2FA tokens.
WWW=		https://github.com/ustayready/CredSniper

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/gnupg \
		??/py-flask@${PY_FLAVOR} \
		??/py-mechanicalsoup@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
