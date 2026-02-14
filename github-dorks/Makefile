PORTNAME=	github-dorks
DISTVERSION=	88.0cfd2cc
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Collection of github dorks and helper tool to automate the process of checking dorks.
WWW=		https://github.com/techgaun/github-dorks

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-deprecated@${PY_FLAVOR} \
		??/py-feedparser@${PY_FLAVOR} \
		??/py-github3.py@${PY_FLAVOR} \
		??/py-pyjwt@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
